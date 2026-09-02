"""
Run: python3 hello_dfs_03_combination_backtrack.py

Recap: step 1 returned answers built from children; step 2 pushed
context (bounds, ranges) down through arguments.

Step 3: combination of state — DFS over a *decision tree* instead of a
data structure. At each call you choose one option, recurse on the rest
of the problem, then undo the choice before trying the next option. The
"state" is the partial solution built so far (a `path` list), mutated in
place: append before recursing, pop right after. This is backtracking —
DFS is the traversal, backtracking is the choose/un-choose discipline.

The mental model: "what are my choices right here, and after each one,
what smaller version of the same problem is left?"

Speedrun (dfs/problems/):
  - medium_39_combination-sum.py
      Watch exactly where `path.append(...)` / `backtrack(...)` /
      `path.pop()` sit relative to each other — that triple is the whole
      pattern.
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    path = []

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
