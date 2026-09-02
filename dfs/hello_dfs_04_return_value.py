"""
Run: python3 hello_dfs_04_return_value.py

Recap: step 2 was trusting a contract for the recursive call; step 3 was
recognizing arguments as state.

Step 4: return value / composition — apply steps 2 and 3 to a tree. A
call's contract is `dfs(node) -> answer`, its state is just `node`, and
the body trusts that contract for `node.left` and `node.right`, then
combines their two answers into this node's answer. No extra state is
threaded through at all.

The mental model: "if I already had the answer for each child, how would
I combine them into the answer for this node?" Then the base case (no
node) is whatever value makes that combination correct for a leaf.

Speedrun after reading this (already solved — trace by hand, don't
rewrite them):
  - dfs/problems/easy_104_maximum-depth-of-binary-tree.py   dfs(node) -> depth
  - dfs/problems/easy_100_same-tree.py                      dfs(p, q) -> bool
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
