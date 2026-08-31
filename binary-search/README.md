# Binary Search

Halve the search space each step by testing the midpoint against a monotonic condition, turning O(n) scans into O(log n).

## When to use
- Searching a sorted (or rotated-sorted) array
- Any problem where you can define a monotonic predicate (`condition(x)` is false...false, true...true) and binary-search on the answer, not just an array index
- Minimizing/maximizing a value subject to a feasibility check ("can we finish in X days?")

## Tips
- Nail the invariant: decide whether `right` is inclusive or exclusive and keep it consistent through every iteration.
- `mid = left + (right - left) // 2` avoids overflow — harmless in Python but idiomatic to carry over.
- Template patterns to memorize: find exact value, find leftmost/rightmost matching value, binary search on the answer space.
- For rotated sorted arrays, at each step one half is guaranteed sorted — check that half first.
- Off-by-one errors are the main bug source — trace a 2-element and 1-element array through your loop before trusting it.
