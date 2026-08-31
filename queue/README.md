# Queue

FIFO structure — the backbone of BFS, and of any problem centered on processing things in arrival order or within a sliding window.

## When to use
- BFS traversal (see [BFS & DFS](../bfs-dfs/README.md))
- Sliding window maximum/minimum via a monotonic deque
- Rate limiting / "recent calls in the last X time" problems
- Producer/consumer simulations

## Tips
- Use `collections.deque` in Python — list `pop(0)` is O(n), deque `popleft()` is O(1).
- Monotonic deque (increasing or decreasing) solves sliding window max/min in O(n) total: pop from the back while it violates the order, pop from the front when it's out of the window range.
- Circular queue implementations need explicit `head`/`tail`/`size` tracking, since `head == tail` alone can't distinguish empty from full.
- A queue of `(timestamp, ...)` pairs with old entries popped from the front handles "count events in the last N seconds" problems.
