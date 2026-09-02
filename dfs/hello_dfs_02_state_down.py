"""
Run: python3 hello_dfs_02_state_down.py

Recap of step 1: dfs(node) -> answer, built from the children's answers.
That's enough when a node's correctness only depends on what's below it.

Step 2: state passed down — some problems need context from *above*:
what the parent already decided, or bounds accumulated along the path
from the root. That context becomes extra parameters on the call, and
each recursive call narrows/updates it before passing it to its children.

The mental model: "what does this node need to know about its ancestors
to check itself?" — then thread that as arguments, not as a return value.

Speedrun:
  - dfs/problems/medium_98_validate-binary-search-tree.py
      dfs(node, low, high) — each child's valid range narrows from the
      parent's, and the node itself is checked against it.
  - dfs/problems/easy_108_convert-sorted-array-to-binary-search-tree.py
      dfs(lo, hi) — the "state" is which slice of the array this call
      owns; children get narrower slices.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(node: Optional[TreeNode], low=float("-inf"), high=float("inf")) -> bool:
    if node is None:
        return True
    if not (low < node.val < high):
        return False
    # state narrows on the way down: node.val becomes the new bound for its side.
    return is_valid_bst(node.left, low, node.val) and is_valid_bst(node.right, node.val, high)


def test_is_valid_bst():
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(valid) is True

    # root=5 but its right child's left child is 3, which violates the
    # bound (3, inf) inherited from being in 5's right subtree.
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(invalid) is False


if __name__ == "__main__":
    test_is_valid_bst()
    print("OK")
