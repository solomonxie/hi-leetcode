"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid
https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

Given an m x n grid where grid[i][j] is 1/2/3/4 (right/left/down/up),
you can follow the arrow for free or pay 1 to change a cell's
direction. Return the minimum cost to travel from (0, 0) to
(m-1, n-1).

Example:
    Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    Output: 3

    Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
    Output: 0
"""
from collections import deque
from typing import List

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # index i means grid value i+1


def minCost(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    cost = [[float("inf")] * cols for _ in range(rows)]
    cost[0][0] = 0
    queue = deque([(0, 0)])  # 0-1 BFS: a deque replaces Dijkstra's heap

    while queue:
        r, c = queue.popleft()
        for i, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                weight = 0 if grid[r][c] == i + 1 else 1
                new_cost = cost[r][c] + weight
                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    if weight == 0:
                        queue.appendleft((nr, nc))  # free edge: explore now
                    else:
                        queue.append((nr, nc))       # cost-1 edge: explore later
    return cost[rows - 1][cols - 1]


def test_minCost():
    assert minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]) == 3
    assert minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]) == 0


if __name__ == "__main__":
    test_minCost()
    print("OK")
