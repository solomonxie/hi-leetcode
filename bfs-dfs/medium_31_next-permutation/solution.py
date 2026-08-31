# https://leetcode.com/problems/next-permutation/
from typing import List


def nextPermutation(nums: List[int]) -> List[int]:
    n = len(nums)
    # find the rightmost index where the sequence starts descending
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        # find the smallest value to the right of i that's still greater than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])  # the suffix is descending; reverse it to get the smallest order
    return nums


if __name__ == "__main__":
    print(nextPermutation([1, 2, 3]))  # [1, 3, 2]
    print(nextPermutation([3, 2, 1]))  # [1, 2, 3]
    print(nextPermutation([1, 1, 5]))  # [1, 5, 1]
