"""
Run: python3 hello_dp_03_tabulate.py

Recap: step 2 cached each state the first time it was computed, on the
way down the recursion.

Step 3: bottom-up tabulation — flip the order. Instead of recursing from
n down to the base case and filling the cache on the way back up, start
at the base case and iterate *up* to n, filling a table in the order
each entry's dependencies are guaranteed to already be there. Same
states, same transition, no recursion, no call stack at all.

The mental model: memo's cache and tabulation's table hold the same
information — the question is only "do I discover I need dp[i] by
recursing down from dp[n], or do I just compute dp[i] for every i in
order because I know dp[n] will need all of them anyway?"

Speedrun:
  - dp/problems/easy_70_climbing-stairs.py
      iterative a, b = b, a + b — bottom-up fib, exactly this step.
  - dp/problems/easy_746_min-cost-climbing-stairs.py
      table indexed by step, each entry built from the two before it.
"""
def fib_table(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # same recurrence as step 2, no recursion
    return dp[n]


def climb_stairs_table(n: int) -> int:
    """1 or 2 steps at a time — dp[i] = ways to reach step i."""
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def test_fib_table():
    assert [fib_table(i) for i in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]


def test_climb_stairs_table():
    assert climb_stairs_table(2) == 2
    assert climb_stairs_table(5) == 8


if __name__ == "__main__":
    test_fib_table()
    test_climb_stairs_table()
    print("OK")
