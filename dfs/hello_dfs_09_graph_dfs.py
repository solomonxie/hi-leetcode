"""
Run: python3 hello_dfs_09_graph_dfs.py

Recap: step 8 added a visited set to stop a grid traversal from looping.

Step 9: graph DFS — the same visited-set trick (step 8), generalized
from a grid's fixed 4-neighbor shape to an arbitrary graph given as an
adjacency list: `graph[node]` is just whatever nodes that node connects
to. A graph may also be disconnected, so the traversal needs an outer
loop that starts a fresh dfs() from every not-yet-visited node — each
such start is one connected component.

The mental model: a grid is secretly a graph where each cell's neighbors
are its 4 adjacent cells; an adjacency list makes that "neighbors"
relationship explicit and arbitrary instead of implied by geometry.

Speedrun:
  - dfs/problems/medium_323_number-of-connected-components-in-an-undirected-graph.py
      Same shape as below, run directly on LeetCode's exact signature.
"""
from typing import List


def count_components(n: int, edges: List[List[int]]) -> int:
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0
    for node in range(n):
        if node not in visited:      # a fresh start = a new component
            count += 1
            dfs(node)
    return count


def test_count_components():
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


if __name__ == "__main__":
    test_count_components()
    print("OK")
