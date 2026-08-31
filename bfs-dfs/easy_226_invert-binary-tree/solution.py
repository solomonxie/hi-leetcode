# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def to_list(root):
    if not root:
        return None
    return [root.val, to_list(root.left), to_list(root.right)]


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(to_list(invertTree(root)))
