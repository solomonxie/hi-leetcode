"""
654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/

Given an integer array nums with no duplicates, build a maximum binary
tree: the root is the maximum number in the array, the left subtree is
built recursively from the subarray to its left, and the right subtree
from the subarray to its right.

Example:
    Input: nums = [3,2,1,6,0,5]
    Output: [6,3,5,null,2,0,null,null,1]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
    def dfs(lo, hi):
        if lo > hi:
            return None
        max_idx = max(range(lo, hi + 1), key=lambda i: nums[i])
        root = TreeNode(nums[max_idx])
        root.left = dfs(lo, max_idx - 1)
        root.right = dfs(max_idx + 1, hi)
        return root

    return dfs(0, len(nums) - 1)


def _to_list(node):
    if not node:
        return None
    return [node.val, _to_list(node.left), _to_list(node.right)]


def test_construct_maximum_binary_tree():
    tree = construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])
    assert _to_list(tree) == [6, [3, None, [2, None, [1, None, None]]], [5, [0, None, None], None]]


if __name__ == "__main__":
    test_construct_maximum_binary_tree()
    print("OK")
