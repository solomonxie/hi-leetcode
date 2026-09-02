"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth - the number of
nodes along the longest path from the root down to the farthest leaf node.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Input: root = [1,null,2]
    Output: 2
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def test_maxDepth():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert maxDepth(root) == 3

    root2 = TreeNode(1, None, TreeNode(2))
    assert maxDepth(root2) == 2


if __name__ == "__main__":
    test_maxDepth()
    print("OK")
