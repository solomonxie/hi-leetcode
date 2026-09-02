"""
Run: python3 hello_dfs_01_return_value.py

Step 1: the recursive shape — a DFS call returns a value built purely
from its children's returned values. No extra state is threaded through
at all; the function signature is just `dfs(node) -> answer`.

The mental model: "if I already had the answer for each child, how would
I combine them into the answer for this node?" Then the base case (no
node) is whatever value makes that combination correct for a leaf.

Speedrun after reading this (in dfs/problems/, already solved — trace
by hand, don't rewrite them):
  - easy_104_maximum-depth-of-binary-tree.py   dfs(node) -> depth
  - easy_100_same-tree.py                      dfs(p, q) -> bool
  - easy_226_invert-binary-tree.py             dfs(node) -> new subtree root
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node: Optional[TreeNode]) -> int:
    # base case: no node -> 0. combine: 1 + the deeper of the two children.
    if node is None:
        return 0
    left = max_depth(node.left)
    right = max_depth(node.right)
    return 1 + max(left, right)


def count_nodes(node: Optional[TreeNode]) -> int:
    # same shape, different combine: sum instead of max.
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def test_max_depth():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(tree) == 3


def test_count_nodes():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert count_nodes(tree) == 5


if __name__ == "__main__":
    test_max_depth()
    test_count_nodes()
    print("OK")
