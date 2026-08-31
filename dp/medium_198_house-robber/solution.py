# https://leetcode.com/problems/house-robber/
from typing import List


def rob(nums: List[int]) -> int:
    prev, curr = 0, 0  # best sum skipping the last house, best sum up to the last house
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))  # 4
    print(rob([2, 7, 9, 3, 1]))  # 12
