set shell := ["bash", "-uc"]

# Show all commands
help:
    @just --list

# Open the command menu
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

# Agent preflight checks
[group('agent')]
agent-preflight:
    @echo "== Git Status =="
    @git status --short
    @echo ""
    @echo "== Available Recipes =="
    @just --list
    @echo ""
    @just check

# Verify repository content after edits
[group('agent')]
agent-verify:
    @just check
    @echo ""
    @echo "== Git Status =="
    @git status --short
    @echo ""
    @echo "== Diff Summary =="
    @git diff --stat

# Show branch, recent commits, and working tree
[group('agent')]
agent-status:
    @echo "== Branch =="
    @git branch --show-current
    @echo ""
    @echo "== Recent Commits =="
    @git log --oneline -5
    @echo ""
    @echo "== Working Tree =="
    @git status --short

# Validate required files, Markdown references, privacy, and release metadata
check:
    @python3 scripts/verify.py
