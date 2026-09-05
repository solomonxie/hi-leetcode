"""
1466. Reorder Routes to Make All Paths Lead to the City Zero
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

n cities are connected by n-1 directed roads that form a tree if you
ignore direction. Return the minimum number of roads that must be
reversed so every city can reach city 0.

Example:
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
"""
from collections import defaultdict, deque
from typing import List


def minReorder(n: int, connections: List[List[int]]) -> int:
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append((b, 1))  # original direction: must reverse to use it
        graph[b].append((a, 0))  # opposite direction: already points toward a

    visited = {0}
    queue = deque([0])
    changes = 0
    while queue:
        node = queue.popleft()
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                changes += cost
                queue.append(neighbor)
    return changes


def test_minReorder():
    assert minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert minReorder(3, [[1, 0], [2, 0]]) == 0


if __name__ == "__main__":
    test_minReorder()
    print("OK")
