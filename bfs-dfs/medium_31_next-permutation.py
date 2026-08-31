"""
31. Next Permutation
https://leetcode.com/problems/next-permutation/

A permutation of an array of integers is an arrangement of its members
into a sequence. The next permutation is the next lexicographically
greater arrangement. If no such arrangement exists (the array is sorted
in descending order), rearrange it as the lowest possible order
(ascending). Must be done in place with O(1) extra memory.

Example:
    Input: nums = [1,2,3]
    Output: [1,3,2]

    Input: nums = [3,2,1]
    Output: [1,2,3]

    Input: nums = [1,1,5]
    Output: [1,5,1]
"""
from typing import List


def nextPermutation(nums: List[int]) -> List[int]:
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


def test_nextPermutation():
    assert nextPermutation([1, 2, 3]) == [1, 3, 2]
    assert nextPermutation([3, 2, 1]) == [1, 2, 3]
    assert nextPermutation([1, 1, 5]) == [1, 5, 1]


if __name__ == "__main__":
    test_nextPermutation()
    print("OK")
