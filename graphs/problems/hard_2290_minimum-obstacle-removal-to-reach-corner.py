"""
2290. Minimum Obstacle Removal to Reach Corner
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

You are given an m x n grid where each cell is 0 (empty) or 1
(obstacle). Moving into an obstacle costs 1 removal; moving into an
empty cell costs 0. Return the minimum number of obstacles to remove to
move from (0, 0) to (m-1, n-1).

Example:
    Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
    Output: 2
"""
from collections import deque
from typing import List


def minimumObstacles(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    cost = [[float("inf")] * cols for _ in range(rows)]
    cost[0][0] = grid[0][0]
    queue = deque([(0, 0)])  # 0-1 BFS: a deque replaces Dijkstra's heap

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = cost[r][c] + grid[nr][nc]
                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    if grid[nr][nc] == 0:
                        queue.appendleft((nr, nc))  # free edge: explore now
                    else:
                        queue.append((nr, nc))       # cost-1 edge: explore later
    return cost[rows - 1][cols - 1]


def test_minimumObstacles():
    assert minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]) == 2
    assert minimumObstacles([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]) == 0


if __name__ == "__main__":
    test_minimumObstacles()
    print("OK")
