"""
Run: python3 hello_dp_07_counting_state.py

Recap: steps 1-6 all *optimized* (min/max) over the table.

Step 7: counting state — the same table shape, but the combine operator
is `+=` instead of `min`/`max`: dp[x] = "number of distinct ways to reach
x," accumulated by summing over every choice that could have produced it.
The new wrinkle is loop order: with an unbounded supply of items (coins
you can reuse), looping *items outer, amount inner* only ever adds a coin
after all combinations without it are settled, so `[1, 2]` and `[2, 1]`
collapse into one combination. Swap the loops (amount outer, coins inner)
and the same table instead counts *permutations* — order would start
mattering, because every amount reconsiders every coin from scratch at
each length.

The mental model: "does trying coin A then coin B count as different from
B then A?" If no (combinations), the item you're allowed to use has to be
fixed for an entire outer pass. If yes (permutations), it doesn't.

Speedrun:
  - dp/problems/medium_518_coin-change-ii.py
      dp[x] = ways to make amount x; coins is the outer loop on purpose.
"""
from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0: use nothing
    for coin in coins:  # outer: "coins allowed so far" — this is what makes it count combinations
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


def count_permutations(amount: int, coins: List[int]) -> int:
    """Same recurrence, loops swapped: counts ordered sequences instead."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for x in range(1, amount + 1):  # outer: amount — every coin is reconsidered at every length
        for coin in coins:
            if coin <= x:
                dp[x] += dp[x - coin]
    return dp[amount]


def test_change_counts_combinations():
    # [1,1,2] and [1,2,1] are the same combination -> counted once.
    assert change(4, [1, 2]) == 3  # {1+1+1+1, 1+1+2, 2+2}
    assert change(5, [1, 2, 5]) == 4


def test_permutations_counts_more():
    # 1+1+2, 1+2+1, 2+1+1 are three distinct orderings of the same coins.
    assert count_permutations(4, [1, 2]) == 5
    assert count_permutations(4, [1, 2]) > change(4, [1, 2])


if __name__ == "__main__":
    test_change_counts_combinations()
    test_permutations_counts_more()
    print("OK")
