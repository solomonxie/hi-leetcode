"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer
target, return a list of all unique combinations of candidates where the
chosen numbers sum to target. The same number may be chosen from
candidates an unlimited number of times.

Example:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
"""
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result


def test_combinationSum():
    assert combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


if __name__ == "__main__":
    test_combinationSum()
    print("OK")
