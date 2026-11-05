# Changelog

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
