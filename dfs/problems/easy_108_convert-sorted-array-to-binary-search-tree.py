"""
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums sorted in ascending order, convert it to a
height-balanced binary search tree.

Example:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted, since either
                 is a height-balanced BST built from the input array.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


def _to_list(root):
    if not root:
        return None
    return [root.val, _to_list(root.left), _to_list(root.right)]


def test_sortedArrayToBST():
    tree = sortedArrayToBST([-10, -3, 0, 5, 9])
    assert _to_list(tree) == [0, [-3, [-10, None, None], None], [9, [5, None, None], None]]


if __name__ == "__main__":
    test_sortedArrayToBST()
    print("OK")
