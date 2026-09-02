"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Given an array of integers nums sorted in ascending order, and an
integer target, write a function to search target in nums. Return its
index, or -1 if not found.

Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    def dfs(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return dfs(mid + 1, hi)
        return dfs(lo, mid - 1)

    return dfs(0, len(nums) - 1)


def test_search():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1


if __name__ == "__main__":
    test_search()
    print("OK")
