"""
Run: python3 hello_dfs_06_structural_state.py

Recap: step 2 passed bounds/ranges down; step 5 ran independent passes
and combined them afterward.

Step 6: state as structure — the "state" a call owns can be an index
range into one or more input arrays, and the return value is a *built
object* (a subtree), assembled from the recursively-built pieces its
children returned. This combines step 1 (return value built from
children) with step 2 (narrowing state passed down) — the two aren't
actually separate tricks, just two ends of the same recursive shape.

A related advanced move: packing more than one fact into a single return
value (e.g. a tuple of `(is_balanced, height)`) so a call can report
both an answer and the context its parent needs, in one trip up —
instead of a separate top-down helper.

The mental model: "what narrower slice does each child own, and what do
I build once I have their two built pieces back?"

Speedrun (dfs/problems/):
  - medium_105_construct-binary-tree-from-preorder-and-inorder-traversal.py
      State = index ranges into `preorder`/`inorder`; each call builds
      one subtree root out of its children's built subtrees.
  - easy_110_balanced-binary-tree.py
      Return value packs two facts at once (height, and whether the
      subtree is balanced) to avoid a second full traversal.
  - easy_572_subtree-of-another-tree.py
      A DFS *nested inside* a DFS: the outer traversal visits every
      node, and at each one runs a second, independent DFS (step 1's
      same-tree check) to compare structures.
"""
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inorder_index = {val: i for i, val in enumerate(inorder)}

    def dfs(pre_lo, pre_hi, in_lo, in_hi):
        # state: which slice of preorder/inorder this call owns.
        if pre_lo > pre_hi:
            return None
        root_val = preorder[pre_lo]
        root_idx = inorder_index[root_val]
        left_size = root_idx - in_lo

        root = TreeNode(root_val)
        # build once both children have built their own pieces
        root.left = dfs(pre_lo + 1, pre_lo + left_size, in_lo, root_idx - 1)
        root.right = dfs(pre_lo + left_size + 1, pre_hi, root_idx + 1, in_hi)
        return root

    return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


def is_balanced(node: Optional[TreeNode]) -> bool:
    def dfs(n) -> Tuple[bool, int]:
        # return value packs two facts: (balanced?, height) in one trip up.
        if n is None:
            return True, 0
        left_ok, left_h = dfs(n.left)
        right_ok, right_h = dfs(n.right)
        balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
        return balanced, 1 + max(left_h, right_h)

    return dfs(node)[0]


def _to_list(node):
    if not node:
        return None
    return [node.val, _to_list(node.left), _to_list(node.right)]


def test_build_tree():
    tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert _to_list(tree) == [3, [9, None, None], [20, [15, None, None], [7, None, None]]]


def test_is_balanced():
    balanced = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(balanced) is True

    unbalanced = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert is_balanced(unbalanced) is False


if __name__ == "__main__":
    test_build_tree()
    test_is_balanced()
    print("OK")
