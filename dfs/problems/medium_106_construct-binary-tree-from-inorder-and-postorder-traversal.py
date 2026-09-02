"""
106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the
inorder traversal of a binary tree and postorder is the postorder
traversal of the same tree, construct and return the binary tree.

Example:
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inorder_index = {val: i for i, val in enumerate(inorder)}

    def dfs(in_lo, in_hi, post_lo, post_hi):
        if in_lo > in_hi:
            return None
        root_val = postorder[post_hi]
        root_idx = inorder_index[root_val]
        left_size = root_idx - in_lo

        root = TreeNode(root_val)
        root.left = dfs(in_lo, root_idx - 1, post_lo, post_lo + left_size - 1)
        root.right = dfs(root_idx + 1, in_hi, post_lo + left_size, post_hi - 1)
        return root

    return dfs(0, len(inorder) - 1, 0, len(postorder) - 1)


def _to_list(node):
    if not node:
        return None
    return [node.val, _to_list(node.left), _to_list(node.right)]


def test_build_tree():
    tree = build_tree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    assert _to_list(tree) == [3, [9, None, None], [20, [15, None, None], [7, None, None]]]


if __name__ == "__main__":
    test_build_tree()
    print("OK")
