# Personal AI resilience starter kit

Use this worksheet to map a personal AI setup, find its shared weak points, and test whether the recovery plan works. Don't put passwords, API keys, authentication tokens, or recovery codes in this file. Record where credentials are managed instead.

## 1. Choose your current level

### Level 1: Stay reachable

"Reachable" means being able to contact your agent and receive its reply through an alternate route when the primary route fails. If your main chat goes down, you can still reach your agent another way.

- [ ] A second communication route is connected.
- [ ] I sent a test message through both routes.
- [ ] I received a reply through both routes.
- [ ] I know whether both routes depend on the same gateway and computer.

If you are new, complete Level 1 before attempting Levels 2 and 3. Do not try to do everything at once.

### Level 2: Stay recoverable

"Recoverable" means you can restore your agent's memory, instructions, configuration, and project files if something breaks or data is lost. If your computer crashes, you have not lost everything.

- [ ] Memory is backed up.
- [ ] Agent instructions are backed up.
- [ ] Configuration is backed up.
- [ ] Project files and unique data are backed up.
- [ ] Recovery notes are stored outside the system they describe.
- [ ] At least one backup is stored away from the main computer.
- [ ] I restored a harmless test file successfully.

If a fully independent backup is not affordable right now, start with what you have. A backup on the same computer is still better than no backup. Add an off-computer or cloud backup when you can. The goal is progressive independence: make backups a little more independent over time, not all at once.

### Level 3: Stay diagnosable

"Diagnosable" means being able to find evidence and understand a failure safely before changing the system. When something breaks, you or a trusted helper can figure out what happened without making things worse.

- [ ] The recovery map below is current.
- [ ] A second agent or trusted person can read the necessary recovery documents.
- [ ] Diagnostic access is read-only by default.
- [ ] Restarts, upgrades, credential changes, configuration edits, and rollbacks require human approval.
- [ ] Only one person or agent makes changes at a time.
- [ ] The result is reviewed after a change.

## 2. AI recovery map

Designated recovery operator (who runs recovery if you are unavailable):

Where this recovery map is stored:

Where the ordered recovery runbook lives (if separate from this map):

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
Record: approved restart command or runbook location, alternate access route, escalation owner, and verification steps.

If the host computer fails:
Record: replacement-host prerequisites, rebuild order (framework, config, instructions, memory, project files), how credentials will be reconnected without putting secrets in the map, and end-to-end recovery verification steps.

If the model provider fails:

If the main account or credentials become unavailable:
Record: where credentials are managed (password manager, vault, or recovery codes), authorized recovery contact, account owner, and provider recovery/escalation instructions. Do not put actual credentials in this map.

## 3. Shared failure-domain worksheet

A "failure domain" is a set of things that fail together because they share the same computer, account, gateway, internet connection, or storage. If one failure can take down two apparently independent systems, they are in the same failure domain.

For each pair, write down what both systems still share.

| Pair being compared | Same computer? | Same gateway? | Same provider account? | Same internet connection? | Same storage? | What one failure could stop both? |
|---|---|---|---|---|---|---|
| Primary and secondary messaging channels | | | | | | |
| Main and backup agents | | | | | | |
| Main and backup models | | | | | | |
| Main files and backups | | | | | | |

Quick test: if both "backups" disappear when you shut down one computer, disable one account, stop one gateway, or disconnect one drive, they aren't independent backups. They may still help with smaller failures, but their limits should be written down.

### What to do after finding shared failure domains

Once you identify a shared weakness, separate one dependency at a time:

- **Same gateway**: add a second route that does not go through the same gateway (e.g., Telegram plus Discord instead of two Telegram bots).
- **Same computer**: move one backup to cloud storage, an external drive, or another machine.
- **Same account**: use a different account or service for the backup path.
- **Same internet connection**: store a backup somewhere reachable without your home network.
- **Same storage**: copy critical files to a different disk or cloud provider.

You do not need to fix everything at once. Each separation reduces risk. Start with the weakest shared dependency and work outward.

## 4. Ten-minute resilience check

How to verify items you may be unsure about:

- "Do both channels depend on the same gateway?" — ask your agent what gateway each channel uses, or check if both channels stop working when you restart the gateway service.
- "Are files backed up?" — check if a backup file exists and is recent: `ls -lh <backup location>`.
- "Can another agent or person read the recovery map?" — ask a second agent or trusted person to find and read the recovery map file without changing anything.

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

Run this drill once per month. Monthly testing is worth the effort because backups, second channels, and recovery instructions can look fine until a real outage exposes that they do not actually work. A monthly drill catches gaps before a real failure does.

### If something fails during the drill

1. Stop. Do not proceed with further risky changes.
2. Restore the disabled route or service immediately.
3. Do not attempt to fix unrelated issues during the drill.
4. Document what failed and what evidence you saw.
5. Fix the gap after the drill is over, in a calm environment.
6. Rerun only the step that failed after the fix is verified.

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