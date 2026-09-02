# BFS

Explore a tree or graph level by level using a queue, expanding the frontier one step at a time. The natural fit whenever "step/level/distance" means something.

## When to use
- Shortest path / minimum steps in an unweighted graph or grid
- Level-order processing (return results grouped by depth)
- "Nearest X from any of several starting points" (multi-source BFS)

## Tips
- Uses a queue (`collections.deque`), not recursion — the frontier is explicit, not implicit in the call stack.
- Always track `visited` explicitly for graphs — trees don't need it since there are no cycles, general graphs do. Mark visited when *pushing*, not when popping, or you'll enqueue duplicates.
- Multi-source BFS (push all sources at once, distance 0) solves "distance from the nearest of several starting points" problems (e.g. rotting oranges).
- For grids, encode visited state as `(row, col)` in a set, or mutate the grid in place if allowed.
- Kahn's algorithm (BFS with in-degree counting) is the BFS route to topological sort — see [sorting](../sorting/README.md).
- Compare with [DFS](../dfs/README.md): same traversal, different order guarantee — BFS gives shortest-path-first, DFS gives full-depth-first.
