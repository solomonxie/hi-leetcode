"""
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

You have a graph of n nodes labeled 0 to n - 1. You are given an integer
n and a list of edges, where edges[i] = [ai, bi] indicates that there is
an undirected edge between ai and bi. Return the number of connected
components in the graph.

Example:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
"""
from typing import List


def countComponents(n: int, edges: List[List[int]]) -> int:
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
        if node not in visited:
            count += 1
            dfs(node)
    return count


def test_countComponents():
    assert countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


if __name__ == "__main__":
    test_countComponents()
    print("OK")
