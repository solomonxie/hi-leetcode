"""
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell is 0 (empty), 1 (fresh
orange), or 2 (rotten orange). Every minute, any fresh orange adjacent
to a rotten one becomes rotten. Return the minimum number of minutes
until no fresh orange remains, or -1 if impossible.

Example:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
"""
from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # multi-source BFS: every rotten orange starts the frontier at minute 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue:
        r, c, minute = queue.popleft()
        minutes = max(minutes, minute)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, minute + 1))

    return minutes if fresh == 0 else -1


def test_oranges_rotting():
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0


if __name__ == "__main__":
    test_oranges_rotting()
    print("OK")
