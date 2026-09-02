"""
Run: python3 hello_dfs_12_path_state.py

Recap: step 11 mutated the input and undid it on the way back up.

Step 12: path state — some problems need context from *above* instead:
what the parent already decided, or bounds accumulated along the path
from the root. Unlike step 11's mutate-and-undo, nothing here is undone
— each call just passes a narrower version of the state forward as a
plain argument, and it's naturally scoped to that call's own subtree
(no shared object, no restore needed).

The mental model: "what does this node need to know about its ancestors
to check itself?" — then thread that as arguments, not as a return value
or a shared/mutated object.

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
