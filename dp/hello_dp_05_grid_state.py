"""
Run: python3 hello_dp_05_grid_state.py

Recap: steps 1-4 all had a state that was a single integer index.

Step 5: 2D grid state — the state is a *position*, `(row, col)`, and the
recurrence pulls from spatial neighbors instead of "one/two steps back
on a line." Two common shapes: a rectangular grid where dp[r][c] comes
from the cell above and the cell to the left, and a triangle where
dp[r][c] comes from the two cells below it. Same core idea as step 4 —
only a fixed-size neighborhood is ever read again — so both still
compress to O(row width) instead of the full grid.

The mental model: "which neighboring cells does this cell's answer come
from?" — draw the grid, mark the arrows, and the recurrence is just
naming those arrows.

Speedrun:
  - dp/problems/medium_62_unique-paths.py
      dp[r][c] = dp[r-1][c] + dp[r][c-1] — paths in from above or from
      the left; compressed to a single reused row.
  - dp/problems/medium_120_triangle.py
      dp[r][c] = triangle[r][c] + min(dp[r+1][c], dp[r+1][c+1]) — built
      bottom-up so both children are already answered.
"""
from typing import List


def unique_paths(m: int, n: int) -> int:
    row = [1] * n  # dp[c] for the current row; row 0 is all 1s (only one way in)
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]  # from above (row[c], not yet updated) + from the left
    return row[-1]


def minimum_total(triangle: List[List[int]]) -> int:
    dp = triangle[-1][:]  # start at the bottom row: dp[c] = cost of that cell alone
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])  # cheaper of the two children below
    return dp[0]


def test_unique_paths():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3


def test_minimum_total():
    assert minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11


if __name__ == "__main__":
    test_unique_paths()
    test_minimum_total()
    print("OK")
