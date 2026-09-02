# Graphs

General graph algorithms beyond simple BFS/DFS traversal: shortest paths with weights, minimum spanning trees, connectivity, and ordering.

## When to use
- Weighted shortest path (Dijkstra, Bellman-Ford)
- Minimum spanning tree (Prim's, Kruskal's)
- Detecting connected components or cycles at scale (Union-Find)
- Dependency ordering (topological sort)

## Tips
- Union-Find (disjoint set) with path compression + union by rank gives near-O(1) connectivity checks — reach for it whenever the problem is "are these connected / will this create a cycle."
- Dijkstra needs non-negative weights and a min-heap of `(distance, node)`; Bellman-Ford handles negative weights and detects negative cycles.
- Topological sort via Kahn's algorithm (BFS + in-degree count) or via DFS post-order reversal — both are worth knowing.
- Represent the graph as an adjacency list (dict of lists) unless density demands a matrix.
- For grids-as-graphs, the "nodes" are cells and edges are the 4 (or 8) neighbors — most grid traversal problems (see [BFS](../bfs/README.md) / [DFS](../dfs/README.md)) are just this in disguise.
