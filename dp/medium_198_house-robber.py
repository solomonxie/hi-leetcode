"""
198. House Robber
https://leetcode.com/problems/house-robber/

You are a robber planning to rob houses along a street. Each house has a
nonnegative amount of money, given in array nums. Adjacent houses have
connected security systems, so you cannot rob two adjacent houses on the
same night. Return the maximum amount of money you can rob without
alerting the police.

Example:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and house 3 (money = 3).
                 Total = 1 + 3 = 4.

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1, house 3, and house 5. Total = 2 + 9 + 1 = 12.
"""
from typing import List


def rob(nums: List[int]) -> int:
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


def test_rob():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12


if __name__ == "__main__":
    test_rob()
    print("OK")
