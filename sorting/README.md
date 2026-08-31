# Sorting

Reordering data — either applying a library sort thoughtfully, or implementing a sort algorithm from scratch when the problem asks for it.

## When to use
- Preprocessing that unlocks a two-pointer/greedy approach
- Custom ordering via comparator (intervals, strings, tuples)
- The problem is directly about a sorting algorithm's mechanics (implement quicksort/mergesort, counting sort, external constraints)

## Tips
- Python's `sorted()`/`list.sort()` (Timsort) is O(n log n) and stable — reach for it by default; only hand-roll a sort when the problem demands a specific algorithm or better bounds (e.g. counting sort for a small integer range).
- Custom comparators via `key=` (or `functools.cmp_to_key` for pairwise comparisons like "largest number formed by concatenation").
- Merge sort's merge step is the building block for "count inversions" and "merge K sorted" problems.
- Quickselect (the partition step of quicksort) finds the Kth smallest/largest in average O(n) — faster than a full sort when only one order statistic is needed.
- Interval problems almost always start with `intervals.sort(key=lambda x: x[0])`.
