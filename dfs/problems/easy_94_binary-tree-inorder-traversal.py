"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its
nodes' values (left, then node, then right).

Example:
    Input: root = [1,null,2,3]
    Output: [1,3,2]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def test_inorder_traversal():
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorder_traversal(tree) == [1, 3, 2]


if __name__ == "__main__":
    test_inorder_traversal()
    print("OK")
