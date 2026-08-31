# https://leetcode.com/problems/subtree-of-another-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def is_same(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return is_same(a.left, b.left) and is_same(a.right, b.right)

    def dfs(node):
        if not node:
            return False
        if is_same(node, subRoot):
            return True
        return dfs(node.left) or dfs(node.right)

    return dfs(root)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    print(isSubtree(root, sub))  # True

    root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    print(isSubtree(root2, sub))  # False
