"""
3418. Maximum Amount of Money Robot Can Earn
https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

You are given an m x n grid coins, where coins[i][j] can be negative (a
gangster steals that amount from the robot) or positive (that amount is
added). The robot starts at (0, 0) and moves only right or down to reach
(m-1, n-1). On at most 2 cells during the journey, the robot can neutralize
the gangster there, so that cell contributes 0 instead of its value. It is
guaranteed there exists a path along which the robot's total money never
goes negative. Return the maximum amount of money the robot can have when
it reaches the final cell.

Example:
    Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
    Output: 8
    Explanation: Path (0,0)->(0,1)->(0,2)->(1,2)->(2,2), neutralizing the
                 -1 at (0,2): 0 + 1 + 0 + 3 + 4 = 8.

    Input: coins = [[10,10,10],[10,10,10]]
    Output: 40
"""
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
                    if i > 0 and dp[i - 1][j][k - 1] != NEG_INF:
                        best = max(best, dp[i - 1][j][k - 1])
                    if j > 0 and dp[i][j - 1][k - 1] != NEG_INF:
                        best = max(best, dp[i][j - 1][k - 1])
                dp[i][j][k] = best

    return dp[m - 1][n - 1][2]


def test_maximumAmount():
    assert maximumAmount([[0, 1, -1], [1, -2, 3], [2, -3, 4]]) == 8
    assert maximumAmount([[10, 10, 10], [10, 10, 10]]) == 40


if __name__ == "__main__":
    test_maximumAmount()
    print("OK")
