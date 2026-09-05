"""
1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary grid, return the length of the shortest clear
path from top-left to bottom-right, moving 8-directionally through
cells with value 0. Return -1 if no such path exists.

Example:
    Input: grid = [[0,1],[1,0]]
    Output: 2
"""
from collections import deque
from typing import List

DIRECTIONS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1

    queue = deque([(0, 0, 1)])
    grid[0][0] = 1   # mark visited by mutating in place

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (n - 1, n - 1):
            return dist
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))
    return -1


def test_shortest_path_binary_matrix():
    assert shortest_path_binary_matrix([[0, 1], [1, 0]]) == 2
    assert shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1


if __name__ == "__main__":
    test_shortest_path_binary_matrix()
    print("OK")
