"""
Run: python3 hello_dp_08_extra_dimension.py

Recap: step 5 was a 2D position; step 6 was a pair of sequence indices;
step 7 reused a 1D table but counted instead of optimized.

Step 8: state gets an extra dimension for a *budget* — how many special
moves are left, how many items you've picked, how much capacity remains.
`dp[i][j][k]` now means "the answer at position (i, j), having used
exactly (or at most) k units of some limited resource." Each layer `k`
is otherwise an ordinary 2D DP (step 5); the new part is that a
transition can either stay on the same layer (an ordinary move) or drop
to a cheaper layer (spend one unit of budget). Base cases get trickier
too: with a budget, "the start" isn't one value but one value *per
layer* (0 uses spent vs. 1 already spent from the very first cell), so
initialize every reachable (i, j, k) at the boundary, not just (0, 0).

The mental model: "if I froze how much budget is left, what 2D DP would
this be?" — answer that per layer, then let transitions move between
layers by spending budget.

Speedrun:
  - dp/problems/medium_3418_maximum-amount-of-money-robot-can-earn.py
      dp[r][c][k] = max money at (r, c) having neutralized k negative
      cells so far (k in 0..2); moving to a negative cell either takes
      the loss (same layer) or spends a neutralization (drops a layer).
"""
NEG_INF = float("-inf")


def max_path_with_skips(grid, max_skips: int) -> int:
    """
    Toy version of the same shape: walk grid[0][0] -> grid[-1][-1] moving
    only right/down, maximizing the sum, but up to `max_skips` cells may
    be skipped (treated as 0) instead of taken at their real value.
    """
    m, n = len(grid), len(grid[0])
    # dp[r][c][k]: best sum reaching (r, c) having used k skips so far
    dp = [[[NEG_INF] * (max_skips + 1) for _ in range(n)] for _ in range(m)]
    for k in range(max_skips + 1):
        dp[0][0][k] = grid[0][0] if k == 0 else max(grid[0][0], 0)

    for r in range(m):
        for c in range(n):
            for k in range(max_skips + 1):
                if r == 0 and c == 0:
                    continue
                best = NEG_INF
                for pr, pc in ((r - 1, c), (r, c - 1)):
                    if pr < 0 or pc < 0:
                        continue
                    # same layer: take this cell's real value
                    best = max(best, dp[pr][pc][k] + grid[r][c])
                    # drop a layer: spend one skip, cell counts as 0
                    if k > 0:
                        best = max(best, dp[pr][pc][k - 1])
                dp[r][c][k] = best
    return max(dp[m - 1][n - 1])


def test_max_path_with_skips_no_budget_is_plain_grid_dp():
    grid = [[1, -5], [1, 1]]
    # 0 skips: forced to eat the -5, or go 1 -> 1 -> 1 = 3 (down, down... only 2x2)
    assert max_path_with_skips(grid, 0) == 3


def test_max_path_with_skips_uses_budget():
    grid = [[1, -5], [1, 1]]
    # 1 skip: can neutralize the -5 on the way through, 1 + 0 + 1 = 2 < 3 still,
    # but on a grid where the direct path is worse than skipping, budget wins.
    grid2 = [[0, -10, 5], [0, 0, 0]]
    assert max_path_with_skips(grid2, 1) > max_path_with_skips(grid2, 0)


if __name__ == "__main__":
    test_max_path_with_skips_no_budget_is_plain_grid_dp()
    test_max_path_with_skips_uses_budget()
    print("OK")
