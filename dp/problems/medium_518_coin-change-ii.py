"""
518. Coin Change II
https://leetcode.com/problems/coin-change-ii/

You are given an integer array coins representing coins of different
denominations (unlimited supply of each) and an integer amount. Return the
number of combinations that make up that amount. Return 0 if that amount
cannot be made up by any combination of the coins.

Example:
    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1.

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: The amount of 3 cannot be made up just with coins of 2.
"""
from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


def test_change():
    assert change(5, [1, 2, 5]) == 4
    assert change(3, [2]) == 0


if __name__ == "__main__":
    test_change()
    print("OK")
