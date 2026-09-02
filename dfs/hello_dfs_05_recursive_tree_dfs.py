"""
Run: python3 hello_dfs_05_recursive_tree_dfs.py

Recap: step 4 built a node's answer from its children's answers —
`dfs(node) -> answer`.

Step 5: recursive tree DFS — that same shape, named. "DFS on a tree"
just means: recurse into left, recurse into right, do something with
the results — depth-first because a call fully finishes one child
(and everything below it) before starting the other. The shape doesn't
change when the return type does: an int (step 4), a bool, or a rebuilt
subtree all fit the same `dfs(node) -> answer` contract.

The mental model: the same one call-shape (visit node, recurse into
children, combine) answers "how deep," "are these equal," and "build me
a mirrored copy" — only the combine step changes.

Speedrun:
  - dfs/problems/easy_572_subtree-of-another-tree.py
      A DFS *nested inside* a DFS: the outer traversal visits every
      node, and at each one calls is_same_tree (below) to compare
      structures.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def invert_tree(node: Optional[TreeNode]) -> Optional[TreeNode]:
    if node is None:
        return None
    node.left, node.right = invert_tree(node.right), invert_tree(node.left)
    return node


def _to_list(node):
    if not node:
        return None
    return [node.val, _to_list(node.left), _to_list(node.right)]


def test_is_same_tree():
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    c = TreeNode(1, TreeNode(2), TreeNode(4))
    assert is_same_tree(a, b) is True
    assert is_same_tree(a, c) is False


def test_invert_tree():
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(tree)
    assert _to_list(inverted) == [4, [7, [9, None, None], [6, None, None]], [2, [3, None, None], [1, None, None]]]


if __name__ == "__main__":
    test_is_same_tree()
    test_invert_tree()
    print("OK")
