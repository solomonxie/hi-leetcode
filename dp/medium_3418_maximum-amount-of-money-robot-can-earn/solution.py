# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/
from typing import List

NEG_INF = float("-inf")


def maximumAmount(coins: List[List[int]]) -> int:
    m, n = len(coins), len(coins[0])
    # dp[i][j][k] = max money reaching (i, j) having used at most k neutralizations (k in 0..2)
    dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
    dp[0][0][0] = coins[0][0]
    dp[0][0][1] = max(coins[0][0], 0)
    dp[0][0][2] = max(coins[0][0], 0)

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            for k in range(3):
                best = NEG_INF
                if i > 0 and dp[i - 1][j][k] != NEG_INF:
                    best = max(best, dp[i - 1][j][k] + coins[i][j])
                if j > 0 and dp[i][j - 1][k] != NEG_INF:
                    best = max(best, dp[i][j - 1][k] + coins[i][j])
                if k > 0:
                    # neutralize this cell: treat its value as 0, spend one neutralization
                    if i > 0 and dp[i - 1][j][k - 1] != NEG_INF:
                        best = max(best, dp[i - 1][j][k - 1])
                    if j > 0 and dp[i][j - 1][k - 1] != NEG_INF:
                        best = max(best, dp[i][j - 1][k - 1])
                dp[i][j][k] = best

    return dp[m - 1][n - 1][2]


if __name__ == "__main__":
    print(maximumAmount([[0, 1, -1], [1, -2, 3], [2, -3, 4]]))  # 8
    print(maximumAmount([[10, 10, 10], [10, 10, 10]]))  # 40
