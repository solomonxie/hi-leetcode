# Array & String

Problems solved by manipulating an array or string directly — in-place rearrangement, hashing for lookups, or a single well-chosen pass — rather than by a named algorithm family like two pointers or DP.

## When to use
- In-place rearrangement under an O(1) extra-space constraint
- Hash map/set for O(1) lookups (frequency counts, seen-before checks)
- Prefix/suffix precomputation to answer a query in one more pass
- The problem's brute force is O(n²) pairwise comparison and a single pass can replace it

## Tips
- A hash map trades space for turning an O(n) lookup into O(1) — reach for it whenever brute force is "for each element, scan the rest."
- In-place array edits (two-pointer overwrite, swap-and-reverse) avoid extra space but usually only work left-to-right or need a defined "next" state to compute.
- For strings, sorting the characters (or a 26-length count array) turns anagram comparisons into O(1) after an O(n log n) or O(n) prep step.
- Prefix sums/products let you answer "aggregate over a range" in O(1) after O(n) precompute — watch for the case that needs a suffix pass too (e.g. product except self).
- KMP's lps (longest-prefix-that's-also-a-suffix) array turns substring search into O(n + m) with no backtracking on the main string, and doubles as the answer to "longest prefix of s that's also a suffix" and (via `s + '#' + reverse(s)`) "longest palindromic prefix" problems.
