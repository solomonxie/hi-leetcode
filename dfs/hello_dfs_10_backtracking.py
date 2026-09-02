"""
Run: python3 hello_dfs_10_backtracking.py

Recap: step 6 built each recursive call's state as an immutable copy
(`path + ch`); step 9 gave DFS a visited set that's never undone.

Step 10: backtracking — DFS over a *decision tree*, where the state is
one mutable `path`, shared and mutated in place instead of copied: choose
(append), recurse, un-choose (pop) before trying the next option. That
append-recurse-pop triple is backtracking; DFS is just the traversal it
runs on. It reaches the same results as step 6's copy-per-call approach,
but reuses one list instead of allocating a new one per call.

The mental model: "what are my choices right here, and after each one,
what smaller version of the same problem is left?" Then undo the choice
so the next option starts from a clean `path`.

Speedrun:
  - dfs/problems/medium_39_combination-sum.py
      Watch exactly where `path.append(...)` / `backtrack(...)` /
      `path.pop()` sit relative to each other — that triple is the whole
      pattern.
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    path = []  # one shared, mutated list — not a fresh copy per call

    def backtrack(start):
        result.append(path[:])  # every path so far is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])       # choose
            backtrack(i + 1)           # recurse on the smaller remaining problem
            path.pop()                 # un-choose, try the next option

    backtrack(0)
    return result


def test_subsets():
    result = subsets([1, 2, 3])
    assert sorted(map(tuple, result)) == sorted(
        map(tuple, [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    )


if __name__ == "__main__":
    test_subsets()
    print("OK")
