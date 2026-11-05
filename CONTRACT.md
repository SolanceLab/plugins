# SolanceLab plugins contract

The store is a list, not a service: it points at plugins that live in their own repositories. It runs nothing and stores nothing itself.

## Doors it offers

| Door | What it answers |
|---|---|
| Plugin marketplace `solancelab` for Claude Code (`.claude-plugin/marketplace.json`) | antechamber, scriptorium, stack-guard, discord, each pinned to its repository's release |
| Plugin marketplace `solancelab` for Codex (`.agents/plugins/marketplace.json`) | the plugins that carry Codex files (today: antechamber) |

## Data it owns

None. Each plugin owns its own data; see its repository's CONTRACT.md.

## Settings and secrets it needs

None. Each plugin names its own.

## Updating

A new plugin release changes one line here: its `ref`. Nothing reaches users until that line changes.
