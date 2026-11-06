# SolanceLab plugins — Copyright (c) 2026 House of Solance. PolyForm Noncommercial 1.0.0. Required Notice: Copyright (c) 2026 House of Solance (https://github.com/SolanceLab)
"""The store's two lists are valid, agree with each other, and point only at SolanceLab repositories."""
import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as fh:
        return json.load(fh)


class Store(unittest.TestCase):
    def setUp(self):
        self.claude = load(".claude-plugin", "marketplace.json")
        self.codex = load(".agents", "plugins", "marketplace.json")

    def sources(self, store):
        return [(p["name"], p["source"]) for p in store["plugins"]]

    def test_both_lists_name_the_store(self):
        self.assertEqual(self.claude["name"], "solancelab")
        self.assertEqual(self.codex["name"], "solancelab")

    def test_every_plugin_points_at_a_solancelab_repository(self):
        for store in (self.claude, self.codex):
            for name, src in self.sources(store):
                self.assertEqual(src["source"], "git-subdir", name)
                self.assertTrue(src["url"].startswith("https://github.com/SolanceLab/"), name)
                self.assertTrue(src["url"].endswith(".git"), name)

    def test_names_are_unique_and_codex_is_a_subset(self):
        claude = [p["name"] for p in self.claude["plugins"]]
        codex = [p["name"] for p in self.codex["plugins"]]
        self.assertEqual(len(claude), len(set(claude)))
        self.assertTrue(set(codex) <= set(claude))

    def test_codex_entries_have_policy_and_category(self):
        for p in self.codex["plugins"]:
            self.assertEqual(p["policy"]["installation"], "AVAILABLE")
            self.assertTrue(p["category"])

    def test_shared_plugins_pin_the_same_release(self):
        claude = {n: s.get("ref") for n, s in self.sources(self.claude)}
        for name, src in self.sources(self.codex):
            self.assertEqual(src.get("ref"), claude[name], name)

    def test_readme_table_lists_every_plugin_with_its_codex_status(self):
        with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
            rows = [l for l in fh.read().splitlines() if l.startswith("| [")]
        codex = {p["name"] for p in self.codex["plugins"]}
        for p in self.claude["plugins"]:
            match = [r for r in rows if p["source"]["url"][:-4] in r]
            self.assertEqual(len(match), 1, p["name"])
            cells = [c.strip() for c in match[0].strip("|").split("|")]
            self.assertEqual(cells[-1] == "yes", p["name"] in codex, p["name"])


if __name__ == "__main__":
    unittest.main()
