"""
Run: python3 hello_dfs_07_shared_state.py

Recap: step 6 gave each recursive call its own copy of the state.

Step 7: shared state across calls — sometimes what you need isn't
naturally a return value (step 4) or a passed-down copy (step 6), it's
one object every call reads and mutates *directly*. Python closures let
an inner dfs() reach outer variables; `nonlocal` is needed to reassign
one (mutating a list/set/dict in place doesn't need it — only rebinding
a plain variable, like this counter, does).

The mental model: "is this state really per-branch (step 3/6), or is it
one running total the whole traversal shares?" Counting and
visited-tracking are almost always shared state, not per-branch state.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_leaves(node: Optional[TreeNode]) -> int:
    total = 0  # shared across every call in this traversal

    def dfs(n):
        nonlocal total
        if n is None:
            return
        if n.left is None and n.right is None:
            total += 1
            return
        dfs(n.left)
        dfs(n.right)

    dfs(node)
    return total


def test_count_leaves():
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert count_leaves(tree) == 3


if __name__ == "__main__":
    test_count_leaves()
    print("OK")
