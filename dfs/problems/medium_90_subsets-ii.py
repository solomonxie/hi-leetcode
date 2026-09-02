"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all
possible subsets (the power set) without duplicate subsets.

Example:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    path = []

    def backtrack(start):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # skip a duplicate choice at this depth
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


def test_subsets_with_dup():
    result = subsets_with_dup([1, 2, 2])
    assert sorted(map(tuple, result)) == sorted(
        map(tuple, [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    )


if __name__ == "__main__":
    test_subsets_with_dup()
    print("OK")
