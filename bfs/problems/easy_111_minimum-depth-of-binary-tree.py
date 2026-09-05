"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth: the number of nodes along
the shortest path from the root down to the nearest leaf node.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 2
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth  # BFS finds the nearest leaf first, no need to keep going
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return 0


def test_min_depth():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert min_depth(tree) == 2
    assert min_depth(TreeNode(1)) == 1
    assert min_depth(None) == 0


if __name__ == "__main__":
    test_min_depth()
    print("OK")
