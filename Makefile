# `make test` checks the store's two plugin lists (Claude Code and Codex).
.PHONY: test
test:
	python3 -m unittest discover -s tests -q

.PHONY: bump bump-check
bump:
	python3 scripts/bump.py

bump-check:
	python3 scripts/bump.py --check
