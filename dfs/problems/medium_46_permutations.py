"""
46. Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.

Example:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
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
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result


def test_permute():
    result = permute([1, 2, 3])
    assert sorted(map(tuple, result)) == sorted(
        map(tuple, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    )


if __name__ == "__main__":
    test_permute()
    print("OK")
