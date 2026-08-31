# Trie (Prefix Tree)

A tree where each path from root to a node spells a prefix, letting you check/insert/search strings in O(length) regardless of how many strings are stored.

## When to use
- Prefix search/autocomplete
- Checking if a word or any prefix of it exists in a dictionary
- Word search problems where many candidate words share prefixes, so shared branches can be pruned together

## Tips
- Each node holds a `children` map (char → node) and an `is_end` flag.
- Combine with DFS/backtracking on a grid (e.g. Word Search II) — the trie lets you abandon a branch the moment no dictionary word matches the prefix so far.
- For memory-sensitive cases, a fixed-size array of 26 children is faster than a dict but wastes space if the alphabet is small in practice.
- Deleting a word means walking down, unmarking `is_end`, and pruning nodes with no children and no `is_end`, from the leaf back up.
