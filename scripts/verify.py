#!/usr/bin/env python3

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "README.md",
    "personal-ai-resilience-starter-kit.md",
    "CHANGELOG.md",
    "LICENSE",
    "AGENTS.md",
    "justfile",
]
TEXT_FILES = REQUIRED + ["scripts/verify.py"]

errors: list[str] = []

for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"missing required file: {relative}")

for relative in TEXT_FILES:
    path = ROOT / relative
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        errors.append(f"missing final newline: {relative}")
    for number, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            errors.append(f"trailing whitespace: {relative}:{number}")

private_patterns = {
    "private home path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "Windows user path": re.compile(r"[A-Za-z]:\\\\Users\\\\[^\\\\]+", re.IGNORECASE),
    "GitHub token": re.compile(r"gh[opusr]_[A-Za-z0-9]{20,}"),
    "API key assignment": re.compile(r"(?i)(api[_-]?key|token|secret)\s*[:=]\s*[A-Za-z0-9_./+-]{16,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}

for relative in TEXT_FILES:
    path = ROOT / relative
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    for label, pattern in private_patterns.items():
        if pattern.search(text):
            errors.append(f"possible {label}: {relative}")

markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for relative in ["README.md", "personal-ai-resilience-starter-kit.md", "CHANGELOG.md"]:
    path = ROOT / relative
    if not path.is_file():
        continue
    for target in markdown_link.findall(path.read_text(encoding="utf-8")):
        target = target.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        if not (ROOT / target).exists():
            errors.append(f"broken local link in {relative}: {target}")

readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
if "releases/latest/download/personal-ai-resilience-starter-kit.md" not in readme:
    errors.append("README is missing the stable release download URL")

kit = (ROOT / "personal-ai-resilience-starter-kit.md").read_text(encoding="utf-8") if (ROOT / "personal-ai-resilience-starter-kit.md").is_file() else ""
for heading in [
    "AI recovery map",
    "Shared failure-domain worksheet",
    "Ten-minute resilience check",
    "Monthly failure drill",
    "Copyable read-only diagnostic prompt",
    "Human approval boundary",
]:
    if heading not in kit:
        errors.append(f"starter kit is missing section: {heading}")

if errors:
    print("Verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Verification passed.")
print(f"Required files: {len(REQUIRED)}")
print("Privacy scan: passed")
print("Markdown references: passed")
print("Starter-kit sections: passed")
