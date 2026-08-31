# BFS & DFS

Two ways to traverse trees, graphs, and grids: BFS explores level by level (shortest path in unweighted graphs), DFS explores as deep as possible before backtracking (reachability, path existence, component structure).

## When to use
- BFS: shortest path/minimum steps in an unweighted graph or grid, level-order processing
- DFS: connected components, cycle detection, topological ordering, exhaustive path exploration, tree traversals

## Tips
- BFS uses a queue; DFS uses a stack (or recursion — watch recursion depth on large inputs).
- Always track `visited` explicitly for graphs — trees don't need it since there are no cycles, general graphs do.
- Multi-source BFS (push all sources at once) solves "distance from the nearest of several starting points" problems (e.g. rotting oranges).
- For grids, encode visited state as `(row, col)` in a set, or mutate the grid in place if allowed.
- DFS on a directed graph with 3 states (unvisited/visiting/visited) detects cycles; 2 states aren't enough.
- Iterative DFS with an explicit stack avoids recursion-limit issues on deep/wide inputs.
