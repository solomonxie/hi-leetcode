# https://leetcode.com/problems/number-of-islands/
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"  # mark visited by sinking the land
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


if __name__ == "__main__":
    grid = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    print(numIslands(grid))  # 1

    grid2 = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    print(numIslands(grid2))  # 3
