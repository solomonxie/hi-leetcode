"""
100. Same Tree
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, return true if they are
structurally identical, and the nodes have the same value.

Example:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Input: p = [1,2], q = [1,null,2]
    Output: false
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def test_isSameTree():
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTree(a, b) is True

    c = TreeNode(1, TreeNode(2))
    d = TreeNode(1, None, TreeNode(2))
    assert isSameTree(c, d) is False


if __name__ == "__main__":
    test_isSameTree()
    print("OK")
