# Two Pointers

Use two indices moving through a sequence (toward each other, or both forward) to avoid nested loops and cut brute-force O(n²) scans down to O(n).

## When to use
- Sorted array/string and you need pairs/triplets meeting a condition
- Comparing from both ends (palindrome checks)
- Removing/partitioning elements in place
- Merging two sorted sequences

## Tips
- Sort first if order doesn't matter — unlocks the "shrink the window from whichever side is too big/small" trick.
- Opposite-direction pointers (`left`/`right`) for sum/target problems on sorted arrays.
- Same-direction pointers (`slow`/`fast`) for in-place filtering, cycle detection, or partitioning.
- Fast/slow pointers at different speeds detect cycles (Floyd's) and find the middle of a linked list.
- Sliding window is a two-pointer variant where the window size grows/shrinks based on a running condition — track a running sum/count instead of recomputing.
- Watch for duplicate values needing a skip step in triplet/quadruplet problems (e.g. 3Sum).
