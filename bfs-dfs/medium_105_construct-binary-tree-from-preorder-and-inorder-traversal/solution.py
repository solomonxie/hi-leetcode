# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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


def to_list(root):
    if not root:
        return None
    return [root.val, to_list(root.left), to_list(root.right)]


if __name__ == "__main__":
    tree = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(to_list(tree))
