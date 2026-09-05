"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order
traversal of its nodes' values (left to right, then right to left for
the next level, alternating).

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result


def test_zigzag_level_order():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert zigzag_level_order(tree) == [[3], [20, 9], [15, 7]]
    assert zigzag_level_order(None) == []


if __name__ == "__main__":
    test_zigzag_level_order()
    print("OK")
