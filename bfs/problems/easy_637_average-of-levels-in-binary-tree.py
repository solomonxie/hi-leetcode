"""
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Given the root of a binary tree, return the average value of the nodes
on each level.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [3.0,14.5,11.0]
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    result = []
    queue = deque([root])
    while queue:
        count = len(queue)
        total = 0
        for _ in range(count):
            node = queue.popleft()
            total += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(total / count)
    return result


def test_average_of_levels():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert average_of_levels(tree) == [3.0, 14.5, 11.0]


if __name__ == "__main__":
    test_average_of_levels()
    print("OK")
