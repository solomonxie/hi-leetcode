"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land)
and '0's (water), return the number of islands. An island is surrounded
by water and is formed by connecting adjacent lands horizontally or
vertically.

Example:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
"""
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


def test_numIslands():
    grid = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert numIslands(grid) == 1

    grid2 = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert numIslands(grid2) == 3


if __name__ == "__main__":
    test_numIslands()
    print("OK")
