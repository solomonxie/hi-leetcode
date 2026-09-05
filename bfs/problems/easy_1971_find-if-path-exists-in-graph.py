"""
1971. Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/

Given a bidirectional graph as an edge list, and a source and
destination node, return true if there is a valid path from source to
destination.

Example:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true

    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
"""
from collections import deque
from typing import List


def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = {source}   # marked when pushed, not when popped
    queue = deque([source])
    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False


def test_valid_path():
    assert valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
    assert valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False


if __name__ == "__main__":
    test_valid_path()
    print("OK")
