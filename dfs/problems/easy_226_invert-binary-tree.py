"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree (mirror it left-to-right
at every node) and return its root.

Example:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Input: root = [2,1,3]
    Output: [2,3,1]
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def _to_list(root):
    if not root:
        return None
    return [root.val, _to_list(root.left), _to_list(root.right)]


def test_invertTree():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    assert _to_list(invertTree(root)) == [
        4,
        [7, [9, None, None], [6, None, None]],
        [2, [3, None, None], [1, None, None]],
    ]


if __name__ == "__main__":
    test_invertTree()
    print("OK")
