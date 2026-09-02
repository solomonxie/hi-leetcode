"""
Run: python3 hello_dp_04_space_compress.py

Recap: step 3 built a full table dp[0..n].

Step 4: space compression — look at the transition, not the table. If
dp[i] only ever reads dp[i-1] and dp[i-2] (a fixed lookback window), the
rest of the table is dead weight the moment you've moved past it. Keep
only the last `k` values in plain variables instead of an array: O(n)
space becomes O(1). The state and the recurrence don't change at all —
only how much of the table you bother keeping.

The mental model: "once dp[i] is computed, which earlier entries will
ever be read again?" If the answer is "none beyond a small fixed window,"
an array is doing more than the problem needs.

Speedrun:
  - dp/problems/easy_746_min-cost-climbing-stairs.py
      `prev, curr = curr, min(...)` — a 2-wide window, no array.
  - dp/problems/medium_198_house-robber.py
      Same rolling-pair trick over a different recurrence (max, not min).
"""
from typing import List


def climb_stairs_compressed(n: int) -> int:
    if n <= 2:
        return n
    prev, curr = 1, 2  # dp[i-2], dp[i-1] — the only two the next step needs
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


def rob_compressed(nums: List[int]) -> int:
    """House robber: max money without robbing two adjacent houses."""
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


def test_climb_stairs_compressed():
    assert climb_stairs_compressed(5) == 8


def test_rob_compressed():
    assert rob_compressed([1, 2, 3, 1]) == 4
    assert rob_compressed([2, 7, 9, 3, 1]) == 12


if __name__ == "__main__":
    test_climb_stairs_compressed()
    test_rob_compressed()
    print("OK")
