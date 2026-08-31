# https://leetcode.com/problems/combination-sum/
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
                break  # sorted, so nothing further can fit either
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)  # i, not i+1: reuse allowed
            path.pop()

    backtrack(0, target, [])
    return result


if __name__ == "__main__":
    print(combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
    print(combinationSum([2, 3, 5], 8))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
