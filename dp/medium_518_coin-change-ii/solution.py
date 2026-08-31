# https://leetcode.com/problems/coin-change-ii/
from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0: choose nothing
    for coin in coins:  # iterate coins on the outside so combinations aren't double-counted as permutations
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


if __name__ == "__main__":
    print(change(5, [1, 2, 5]))  # 4
    print(change(3, [2]))  # 0
