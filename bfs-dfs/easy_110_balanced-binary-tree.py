"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced - for every node,
the height difference between its left and right subtrees is at most 1.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


def test_isBalanced():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert isBalanced(root) is True

    root2 = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2),
    )
    assert isBalanced(root2) is False


if __name__ == "__main__":
    test_isBalanced()
    print("OK")
