"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the
preorder traversal of a binary tree and inorder is the inorder traversal
of the same tree, construct and return the binary tree.

Example:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inorder_index = {val: i for i, val in enumerate(inorder)}
    pre_idx = [0]  # mutable cursor into preorder, shared across recursive calls

    def build(left, right):
        if left > right:
            return None
        root_val = preorder[pre_idx[0]]
        pre_idx[0] += 1
        root = TreeNode(root_val)
        mid = inorder_index[root_val]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    return build(0, len(inorder) - 1)


def _to_list(root):
    if not root:
        return None
    return [root.val, _to_list(root.left), _to_list(root.right)]


def test_buildTree():
    tree = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert _to_list(tree) == [3, [9, None, None], [20, [15, None, None], [7, None, None]]]


if __name__ == "__main__":
    test_buildTree()
    print("OK")
