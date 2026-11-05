# `make test` checks the store's two plugin lists (Claude Code and Codex).
.PHONY: test
test:
	python3 -m unittest discover -s tests -q
