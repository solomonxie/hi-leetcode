"""
Run: python3 hello_dfs_01_recursion.py

Step 1: recursion — a function that calls itself on a smaller version of
the same problem, until it hits a base case small enough to answer
directly. Two parts, always: a base case (stop and return) and a
recursive case (do a little work, then call yourself on less work).

The mental model: each call is a fresh stack frame with its own local
variables. `factorial(4)` doesn't compute anything itself — it asks
`factorial(3)` for an answer, multiplies it by 4, and returns that up.
The call stack *is* the mechanism; nothing here is DFS-specific yet.

Speedrun (plain recursion, no tree/graph needed yet — trace by hand):
  - dfs/problems/easy_509_fibonacci-number.py
  - dfs/problems/easy_70_climbing-stairs.py
  - dfs/problems/easy_326_power-of-three.py
  - dfs/problems/easy_344_reverse-string.py
  - dfs/problems/easy_206_reverse-linked-list.py
  - dfs/problems/easy_21_merge-two-sorted-lists.py
  - dfs/problems/medium_50_powx-n.py
  - dfs/problems/medium_24_swap-nodes-in-pairs.py
  - dfs/problems/easy_203_remove-linked-list-elements.py
  - dfs/problems/easy_704_binary-search.py
"""


def factorial(n: int) -> int:
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case: smaller problem + a little work


def sum_to_n(n: int) -> int:
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)


def test_factorial():
    assert factorial(1) == 1
    assert factorial(4) == 24


def test_sum_to_n():
    assert sum_to_n(0) == 0
    assert sum_to_n(5) == 15


if __name__ == "__main__":
    test_factorial()
    test_sum_to_n()
    print("OK")
