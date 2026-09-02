"""
129. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/

Each root-to-leaf path represents a number formed by concatenating its
digits. Given the root of a binary tree containing digits 0-9, return
the total sum of all root-to-leaf numbers.

Example:
    Input: root = [1,2,3]
    Output: 25

    Input: root = [4,9,0,5,1]
    Output: 1026
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: Optional[TreeNode]) -> int:
    def dfs(node, running):
        if node is None:
            return 0
        running = running * 10 + node.val   # state passed down, narrowed each call
        if node.left is None and node.right is None:
            return running
        return dfs(node.left, running) + dfs(node.right, running)

    return dfs(root, 0)


def test_sum_numbers():
    assert sum_numbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25
    tree = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    assert sum_numbers(tree) == 1026


if __name__ == "__main__":
    test_sum_numbers()
    print("OK")
