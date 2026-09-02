"""
47. Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

Example:
    Input: nums = [1,1,2]
    Output: [[1,1,2],[1,2,1],[2,1,1]]
"""
from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue  # skip a duplicate choice at this depth
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result


def test_permute_unique():
    result = permute_unique([1, 1, 2])
    assert sorted(map(tuple, result)) == sorted(map(tuple, [[1, 1, 2], [1, 2, 1], [2, 1, 1]]))


if __name__ == "__main__":
    test_permute_unique()
    print("OK")
