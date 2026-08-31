"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary
search tree (BST). A valid BST is defined as: every node's left subtree
contains only values strictly less than the node's value, every node's
right subtree contains only values strictly greater, and both subtrees
must also be BSTs.

Example:
    Input: root = [2,1,3]
    Output: true

    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root's value is 5 but its right child's left child
                 is 3, which is less than 5.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))


def test_isValidBST():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert isValidBST(root) is True

    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert isValidBST(root2) is False


if __name__ == "__main__":
    test_isValidBST()
    print("OK")
