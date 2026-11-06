# SolanceLab plugins

Made by House of Solance · free for noncommercial use · credit required

## What it is

One plugin store with every plugin House of Solance publishes, for Claude Code and for Codex. Each plugin lives in its
own repository; this store only points at them, so you add one store and see them all.

## Plugins

| Plugin | What it does | Claude Code | Codex |
|---|---|---|---|
| [antechamber](https://github.com/SolanceLab/antechamber) | Recall for your AI: one question searches every store you connect and returns only the best matches. Runs on your own computer; claude.ai and ChatGPT can reach it through its remote door (see its README). | yes | yes |
| [scriptorium](https://github.com/SolanceLab/scriptorium) | Turns your chat history into memories you can check, with their exact words, source lines and real dates. | yes | coming |
| [stack-guard](https://github.com/SolanceLab/stack-guard) | Checks what you run for known security holes, explains them in plain words, and applies the safe fixes after your yes. | yes | coming |
| [discord](https://github.com/SolanceLab/tertulia-ai-discord-engine) (Tertúlia) | Discord tools for your AI: messages, files, reactions, polls, threads, forums, moderation. | yes | coming |
| [vault-map](https://github.com/SolanceLab/vault-map) | Ask where you wrote about something and get the passage back, from a map of your markdown or Obsidian vault. Runs on your own computer; nothing leaves it. | yes | yes |

For Antechamber and Scriptorium together as one memory set, see [presence-app](https://github.com/SolanceLab/presence-app).

## What you need

- Claude Code, or the Codex app or command line.
- Whatever each plugin's own README asks for: most plugins are the connection and the instructions, and the server or
  tool they talk to is set up from that plugin's repository.

## Install

**Claude Code:**

```
claude plugin marketplace add SolanceLab/plugins
claude plugin install antechamber@solancelab
```

**Codex:** in the app, Plugins, Add, Add a marketplace, source `SolanceLab/plugins`. Or from the command line:

```
codex plugin marketplace add SolanceLab/plugins
codex plugin add antechamber@solancelab
```

## Settings

The store has none. In Claude Code each plugin asks for its own settings when you install it. Codex has no settings
prompt, so its plugins point at the default local address and read their key from an environment variable named in
each plugin's README (Antechamber: `ANTECHAMBER_MCP_KEY`).

## Tools

The store adds no tools of its own; each plugin brings its tools and skills, listed in its README.

## Updates

Third-party marketplaces do not auto-update by default. To turn it on once in Claude Code:
`/plugin` > Marketplaces > `solancelab` > Enable auto-update.
To update by hand: `claude plugin marketplace update solancelab`, then `claude plugin update <plugin>@solancelab`, then
restart. In Codex: `codex plugin marketplace upgrade solancelab`.
Each plugin is pinned to its release's exact commit; if a release tag is ever moved, the job refuses to run and changes nothing.

The store updates itself: a daily job moves each plugin to its newest release, runs the store tests, and commits only when they pass.
A plugin only moves when its new version is published as a GitHub Release; a bare version tag is ignored.

Each plugin may also tell you itself when a newer version is out; its README says how, and how to switch that off.

## Limits

- Codex lists only the plugins that carry Codex files; the others say "coming" above.
- The store points at fixed releases. A plugin's newest changes reach you when its release here is updated.

## How it works

`.claude-plugin/marketplace.json` is the list Claude Code reads and `.agents/plugins/marketplace.json` the one Codex
reads. Each entry names a plugin, its repository, the folder it lives in and the release it is pinned to. `make test`
checks that both lists are valid, agree with each other, and point only at SolanceLab repositories.

## Credit and use

The store and its descriptions are made by House of Solance. You're welcome to use it, change it and build on it for
any noncommercial purpose, as long as our credit travels with it. Each plugin keeps its own licence, in its own
repository.

**Keep the credit.** Every copy, changed or not, must carry the licence and this line:
`Required Notice: Copyright (c) 2026 House of Solance (https://github.com/SolanceLab)`

**Commercial use needs our permission.** Ask us first.

## Licence

[PolyForm Noncommercial 1.0.0](LICENSE.md). See [NOTICE.md](NOTICE.md).
