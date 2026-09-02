"""
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X is good if, in the path from the
root to X, there is no node with a value greater than X's value. Return
the number of good nodes.

Example:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: Optional[TreeNode]) -> int:
    count = 0  # shared across the whole traversal

    def dfs(node, path_max):
        nonlocal count
        if node is None:
            return
        if node.val >= path_max:
            count += 1
        dfs(node.left, max(path_max, node.val))
        dfs(node.right, max(path_max, node.val))

    dfs(root, float("-inf"))
    return count


def test_good_nodes():
    tree = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    assert good_nodes(tree) == 4


if __name__ == "__main__":
    test_good_nodes()
    print("OK")
