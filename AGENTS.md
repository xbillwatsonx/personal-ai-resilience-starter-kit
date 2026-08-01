# Repository instructions

This is a documentation-only public repository for the Personal AI Resilience Starter Kit.

## Justfile-first rule

Before operational work:

1. Run `just help` or `just --list`.
2. Run `just agent-preflight` before editing.
3. Use an existing recipe when one matches the task.
4. Run `just agent-verify` after edits.
5. Propose a new recipe when a workflow becomes repeatable.

## Boundaries

- Keep the starter kit beginner-friendly and platform-neutral.
- Never add real credentials, tokens, private hostnames, personal paths, or completed recovery maps.
- Keep examples read-only by default and require human approval before changes.
- Do not add application code, telemetry, account setup, or automated system modification.
- Update `CHANGELOG.md` for released changes.
