"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if
there is a subtree of root with the same structure and node values as
subRoot, and false otherwise. A subtree of a tree is a tree consisting of
a node in the tree and all of that node's descendants.

Example:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def is_same(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return is_same(a.left, b.left) and is_same(a.right, b.right)

    def dfs(node):
        if not node:
            return False
        if is_same(node, subRoot):
            return True
        return dfs(node.left) or dfs(node.right)

    return dfs(root)


def test_isSubtree():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    assert isSubtree(root, sub) is True

    root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    assert isSubtree(root2, sub) is False


if __name__ == "__main__":
    test_isSubtree()
    print("OK")
