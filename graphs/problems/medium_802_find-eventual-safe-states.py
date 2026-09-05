"""
802. Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/

There are n nodes in a directed graph, graph[i] is the list of nodes
node i points to. A node is safe if every possible path starting there
eventually leads to a terminal node (no path from it ever reaches a
cycle). Return all safe nodes in ascending order.

Example:
    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]
"""
from collections import deque
from typing import List


def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    reverse = [[] for _ in range(n)]
    out_degree = [0] * n
    for node, neighbors in enumerate(graph):
        out_degree[node] = len(neighbors)
        for neighbor in neighbors:
            reverse[neighbor].append(node)

    # Kahn's algorithm run backwards: a terminal node (out-degree 0) is
    # trivially safe; peeling it off can make its predecessors safe too.
    safe = [False] * n
    queue = deque(node for node in range(n) if out_degree[node] == 0)
    while queue:
        node = queue.popleft()
        safe[node] = True
        for predecessor in reverse[node]:
            out_degree[predecessor] -= 1
            if out_degree[predecessor] == 0:
                queue.append(predecessor)

    return [node for node in range(n) if safe[node]]


def test_eventualSafeNodes():
    assert eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]
    assert eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) == [4]


if __name__ == "__main__":
    test_eventualSafeNodes()
    print("OK")
