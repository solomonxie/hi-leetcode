# Heap (Priority Queue)

A binary heap gives O(log n) insert and O(1) peek at the min (or max) element — the tool of choice whenever you need the "top/bottom K" repeatedly.

## When to use
- Kth largest/smallest element, top-K frequent
- Merging K sorted lists/streams
- Running median from a data stream
- Task scheduling / Dijkstra's shortest path

## Tips
- Python's `heapq` is a min-heap only — negate values to simulate a max-heap.
- Keep the heap size capped at K when you only need the top/bottom K — push then pop when it exceeds K, so it stays O(n log k) instead of O(n log n).
- Two heaps (a max-heap for the lower half, a min-heap for the upper half) is the standard trick for a running median.
- For "merge K sorted" problems, seed the heap with one element per list, tagged with its source index, and push the next element from that source each time you pop.
- Store tuples `(priority, tiebreaker, item)` when items aren't directly comparable, to avoid comparison errors on ties.
