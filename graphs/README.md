# Graphs

General graph algorithms beyond simple BFS/DFS traversal: shortest paths with weights, minimum spanning trees, connectivity, and ordering.

## When to use
- Weighted shortest path (Dijkstra, Bellman-Ford, bounded-stop relaxation)
- Edge weights are only 0/1 (0-1 BFS) — shortest path without a heap
- Minimum spanning tree / cheapest way to connect everything (Prim's, Kruskal's)
- Detecting connected components or cycles at scale (Union-Find)
- Reachability: "can every node reach X" / "which nodes are safe" (peel from the terminal end)
- Dependency ordering (topological sort)

## Tips
- Union-Find (disjoint set) with path compression + union by rank gives near-O(1) connectivity checks — reach for it whenever the problem is "are these connected / will this create a cycle."
- Dijkstra needs non-negative weights and a min-heap of `(distance, node)`; Bellman-Ford handles negative weights and detects negative cycles, and also bounds the number of edges used (relax for exactly k+1 rounds off the previous round's distances).
- 0-1 BFS replaces Dijkstra's heap with a plain deque when every edge costs 0 or 1: push a 0-cost neighbor to the front (explore it next) and a 1-cost neighbor to the back — same O(V+E) as plain BFS, no log factor.
- Topological sort via Kahn's algorithm (BFS + in-degree count) or via DFS post-order reversal — both are worth knowing. Running Kahn's on the *reverse* graph from out-degree-0 nodes peels off "eventually safe" nodes the same way.
- Represent the graph as an adjacency list (dict of lists) unless density demands a matrix.
- For grids-as-graphs, the "nodes" are cells and edges are the 4 (or 8) neighbors — most grid traversal problems (see [BFS](../bfs/README.md) / [DFS](../dfs/README.md)) are just this in disguise.
