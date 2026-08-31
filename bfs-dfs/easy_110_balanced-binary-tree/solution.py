# https://leetcode.com/problems/balanced-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def height(node):
        # returns -1 if the subtree rooted at `node` is already unbalanced
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(isBalanced(root))  # True

    root2 = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2),
    )
    print(isBalanced(root2))  # False
