# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    node = root
    while stack or node:
        while node:  # walk to the leftmost unvisited node
            stack.append(node)
            node = node.left
        node = stack.pop()  # inorder traversal visits nodes in ascending order for a BST
        k -= 1
        if k == 0:
            return node.val
        node = node.right


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(kthSmallest(root, 1))  # 1

    root2 = TreeNode(
        5,
        TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
        TreeNode(6),
    )
    print(kthSmallest(root2, 3))  # 3
