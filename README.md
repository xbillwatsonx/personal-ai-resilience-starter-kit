# Personal AI Resilience Starter Kit

A practical worksheet for mapping a personal AI setup, finding shared weak points, and testing whether the recovery plan works.

This kit grew out of a real failure: an AI agent received a Telegram message and generated a reply, but the outbound reply was never delivered. A second communication route through Discord kept the agent reachable while the Telegram path was investigated.

## Use the kit

- [Read or copy the starter kit](personal-ai-resilience-starter-kit.md)
- [Download the latest release](https://github.com/xbillwatsonx/personal-ai-resilience-starter-kit/releases/latest/download/personal-ai-resilience-starter-kit.md)

The downloadable file includes:

- three levels of protection: reachable, recoverable, and diagnosable
- an AI recovery-map template
- a shared failure-domain worksheet
- a 10-minute resilience check
- a monthly failure drill
- a copyable read-only diagnostic prompt
- a human-approval boundary worksheet

## Quick start

1. Download or copy `personal-ai-resilience-starter-kit.md`.
2. Save your working copy somewhere private.
3. Fill in the recovery map without recording passwords, API keys, tokens, or recovery codes.
4. Run the 10-minute check.
5. Test one harmless restore and one alternate communication route.
6. Update the map whenever the system changes.

## Keep completed copies private

The blank template is safe to share. A completed recovery map may reveal computer names, providers, file locations, backup locations, or other infrastructure details. Don't commit a completed copy to a public repository.

## What this kit does not guarantee

A second channel, backup, agent, or host reduces the effect of some failures. None of them guarantees uptime or correct recovery. Two apparent backups may still depend on the same computer, gateway, provider account, internet connection, or storage device.

Use the worksheet to identify those shared dependencies and decide which ones matter for your setup.

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE). You can share and adapt it with attribution.
