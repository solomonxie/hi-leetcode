"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its
nodes' values (node, then left, then right).

Example:
    Input: root = [1,null,2,3]
    Output: [1,2,3]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if node is None:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def test_preorder_traversal():
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert preorder_traversal(tree) == [1, 2, 3]


if __name__ == "__main__":
    test_preorder_traversal()
    print("OK")
