"""
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible
subsets (the power set). The solution set must not contain duplicate
subsets.

Example:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    path = []

    def backtrack(start):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

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
