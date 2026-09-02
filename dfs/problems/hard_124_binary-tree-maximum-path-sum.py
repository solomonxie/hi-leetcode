"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given the root of a binary tree, return the maximum path sum of any
non-empty path, where a path may start and end at any node and does not
need to pass through the root.

Example:
    Input: root = [1,2,3]
    Output: 6

    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def dfs(node):
        nonlocal best
        if node is None:
            return 0
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)
        best = max(best, node.val + left_gain + right_gain)
        # the value this call reports up: a single branch, not both.
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return best


def test_max_path_sum():
    assert max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
    tricky = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(tricky) == 42


if __name__ == "__main__":
    test_max_path_sum()
    print("OK")
