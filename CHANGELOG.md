# Changelog

## 1.2.2

Pins moved to the newest releases: stack-guard v1.7.0 → v1.7.1.

## 1.2.1

Pins moved to the newest releases: antechamber v1.2.0 → v1.2.1.

## 1.2.0

stack-guard 1.7.0 and Tertúlia 1.7.0 are pinned to their releases and now listed for Codex too. Tertúlia's plugin is named tertulia-ai-discord-engine (it was listed as discord, unpinned). If you installed `discord@solancelab`, move over by uninstalling it and installing the new name: `claude plugin uninstall discord@solancelab` then `claude plugin install tertulia-ai-discord-engine@solancelab`. Your server address and key settings are asked for again. The weekly dependency check now covers only the workflows, so it stops failing on package files the store does not have.

## 1.1.0

The store lists five more rooms, each in both lists (Claude Code and Codex): vault-map, solance-canvas, claude-config-dashboard, escutario and garmin-mcp-cloud. Every entry is pinned to its release commit. A test keeps the README table and both lists in step. Antechamber is pinned to 1.2.0 (it starts itself in Claude Code and Codex).

## 1.0.1

Pins moved to the newest releases: scriptorium v1.0.0 → v1.1.0.

## 1.0.4

The daily update writes the matching changelog heading when it moves a pin, and Makefile pins carry their release commit too.

## 1.0.3

The daily update trusts only published GitHub Releases, never a bare tag.

## 1.0.2

Each plugin is pinned to its release's commit (`sha`); the daily job refuses to run, and changes nothing, when a release tag no longer points at the recorded commit (`python3 scripts/bump.py --pin-shas` records shas).

## 1.0.1

The store updates itself: a daily job moves each plugin to its newest release, runs the store tests, and commits only when they pass (`scripts/bump.py`, `make bump`).

## 1.0.0

First release: one store for every plugin House of Solance publishes, in both formats (Claude Code `.claude-plugin/marketplace.json`, Codex `.agents/plugins/marketplace.json`). Listed: antechamber, scriptorium, stack-guard, discord (Tertúlia); Codex: antechamber.
