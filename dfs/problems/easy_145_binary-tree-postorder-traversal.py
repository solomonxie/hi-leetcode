"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its
nodes' values (left, then right, then node).

Example:
    Input: root = [1,null,2,3]
    Output: [3,2,1]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result


def test_postorder_traversal():
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert postorder_traversal(tree) == [3, 2, 1]


if __name__ == "__main__":
    test_postorder_traversal()
    print("OK")
