# Personal AI resilience starter kit

Use this worksheet to map a personal AI setup, find its shared weak points, and test whether the recovery plan works. Don't put passwords, API keys, authentication tokens, or recovery codes in this file. Record where credentials are managed instead.

## 1. Choose your current level

### Level 1: Stay reachable

- [ ] A second communication route is connected.
- [ ] I sent a test message through both routes.
- [ ] I received a reply through both routes.
- [ ] I know whether both routes depend on the same gateway and computer.

### Level 2: Stay recoverable

- [ ] Memory is backed up.
- [ ] Agent instructions are backed up.
- [ ] Configuration is backed up.
- [ ] Project files and unique data are backed up.
- [ ] Recovery notes are stored outside the system they describe.
- [ ] At least one backup is stored away from the main computer.
- [ ] I restored a harmless test file successfully.

### Level 3: Stay diagnosable

- [ ] The recovery map below is current.
- [ ] A second agent or trusted person can read the necessary recovery documents.
- [ ] Diagnostic access is read-only by default.
- [ ] Restarts, upgrades, credential changes, configuration edits, and rollbacks require human approval.
- [ ] Only one person or agent makes changes at a time.
- [ ] The result is reviewed after a change.

## 2. AI recovery map

Main agent:

Agent framework:

Host computer or server:

Primary messaging channel:

Secondary messaging channel:

Model provider:

Backup model provider, if any:

Gateway or main service:

How to check its status:

Log location:

Memory location:

Instructions location:

Configuration location:

Project files:

Backup location:

Date of last successful backup:

Date of last successful restore test:

Who has read-only diagnostic access:

Changes that require human approval:

If the main messaging channel fails:

If the gateway fails:

If the host computer fails:

If the model provider fails:

If the main account or credentials become unavailable:

## 3. Shared failure-domain worksheet

For each pair, write down what both systems still share.

| Pair being compared | Same computer? | Same gateway? | Same provider account? | Same internet connection? | Same storage? | What one failure could stop both? |
|---|---|---|---|---|---|---|
| Primary and secondary messaging channels | | | | | | |
| Main and backup agents | | | | | | |
| Main and backup models | | | | | | |
| Main files and backups | | | | | | |

Quick test: if both "backups" disappear when you shut down one computer, disable one account, stop one gateway, or disconnect one drive, they aren't independent backups. They may still help with smaller failures, but their limits should be written down.

## 4. Ten-minute resilience check

- [ ] Can I reach my main agent through a second channel?
- [ ] Have I received a reply through both channels recently?
- [ ] Do both channels depend on the same gateway or computer?
- [ ] Are memory, instructions, configuration, and project files backed up?
- [ ] Is at least one backup stored away from the main computer?
- [ ] Have I restored a harmless test file successfully?
- [ ] Can another agent or person read the recovery map without changing the system?
- [ ] Do risky actions require my approval?

Every unchecked item is a specific place to improve. It doesn't mean the whole setup has failed.

## 5. Monthly failure drill

Date:

Person supervising the drill:

### Communication test

- [ ] Send a message through the primary channel and receive a reply.
- [ ] Send a message through the secondary channel and receive a reply.
- [ ] Temporarily disable one route without changing the agent itself.
- [ ] Confirm the other route still works.
- [ ] Restore the disabled route.

### Recovery test

- [ ] Confirm that the latest backup exists.
- [ ] Restore one harmless test file to a temporary location.
- [ ] Open the restored file and verify its contents.
- [ ] Remove the temporary test copy when finished.

### Diagnostic test

- [ ] Ask the second agent or trusted person to locate the recovery map.
- [ ] Confirm that required logs and status information can be found.
- [ ] Confirm that diagnostic access remains read-only.
- [ ] Record missing, stale, or unclear instructions.

### Drill result

What worked:

What failed:

What was unclear:

What needs to be updated:

Who approved any changes:

Date the recovery map was updated:

## 6. Copyable read-only diagnostic prompt

> Inspect my AI setup in read-only mode. Map the single points of failure across messaging, model providers, the host computer, gateways, credentials, memory, configuration, project files, and backups. Identify shared dependencies that could stop more than one apparent backup at the same time. Verify what you can inspect and clearly label anything you cannot access. Do not expose secrets. Do not change files, settings, services, sessions, credentials, or running processes. Propose a second communication route, a backup plan, and a small recovery runbook. Explain the plan in plain language and stop for my approval before making any changes.

## 7. Human approval boundary

Write down the actions that nobody should take automatically:

- Configuration changes:
- Service restarts:
- Software upgrades:
- Credential changes:
- Session resets:
- Backup restoration:
- Rollbacks:
- File deletion:
- Other:

The agents can inspect, compare evidence, and propose a repair. The human assigns the work and approves the change.

---

**Source:** [Personal AI Resilience Starter Kit](https://github.com/xbillwatsonx/personal-ai-resilience-starter-kit)

Licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). You may share and adapt this kit with attribution.
