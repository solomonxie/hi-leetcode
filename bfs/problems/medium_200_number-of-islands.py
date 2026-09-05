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
"""
from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                grid[r][c] = "0"   # mark visited when pushing, not when popping
                queue = deque([(r, c)])
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))
    return count


def test_num_islands():
    grid = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert num_islands(grid) == 1

    grid2 = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(grid2) == 3


if __name__ == "__main__":
    test_num_islands()
    print("OK")
