"""
785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

Given an undirected graph as an adjacency list, return true if it is
bipartite: its nodes can be split into two sets so every edge connects
nodes from different sets.

Example:
    Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: false

    Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    Output: true
"""
from collections import deque
from typing import List


def is_bipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [0] * n   # 0 = uncolored, 1 / -1 = the two sides

    for start in range(n):
        if color[start] != 0:
            continue
        color[start] = 1
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == color[node]:
                    return False
                if color[neighbor] == 0:
                    color[neighbor] = -color[node]   # opposite side of its parent
                    queue.append(neighbor)
    return True


def test_is_bipartite():
    assert is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
    assert is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True


if __name__ == "__main__":
    test_is_bipartite()
    print("OK")
