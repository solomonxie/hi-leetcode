"""
Run: python3 hello_dfs_13_complex_state.py

Recap: every step so far has been one technique in isolation — return
value, shared state, visited, path state. Real problems mix them.

Step 13: more complex state — two ways techniques combine:

  1. Independent passes: run DFS more than once, each pass with its own
     fresh shared state (step 7/8, repeated), then combine the results
     afterward. The passes don't interfere because each gets its own
     visited set; only the combining step ties them together.

  2. Structural state + built return value: a call's state (step 12) is
     an index range into the input, and its return value (step 4) is a
     *built object* assembled from its children's built pieces — the
     two aren't separate tricks, just two ends of the same recursive
     shape. A return value can also pack more than one fact at once
     (e.g. `(is_balanced, height)`) so a call reports both an answer and
     the context its parent needs, in one trip up.

The mental model: "can I answer this with one traversal whose state means
two things at once, or is it cleaner as separate passes/facts, combined
at the end?" Usually splitting is easier to reason about correctly.

Speedrun:
  - dfs/problems/medium_417_pacific-atlantic-water-flow.py
      Two independent DFS sweeps — Pacific-facing border, Atlantic-facing
      border — each with its own visited set, intersected at the end.
  - dfs/problems/medium_105_construct-binary-tree-from-preorder-and-inorder-traversal.py
      State = index ranges into preorder/inorder; each call builds one
      subtree root out of its children's built subtrees.
  - dfs/problems/easy_110_balanced-binary-tree.py
  - dfs/problems/easy_108_convert-sorted-array-to-binary-search-tree.py
  - dfs/problems/medium_98_validate-binary-search-tree.py
  - dfs/problems/medium_129_sum-root-to-leaf-numbers.py
  - dfs/problems/medium_106_construct-binary-tree-from-inorder-and-postorder-traversal.py
  - dfs/problems/medium_654_maximum-binary-tree.py
  - dfs/problems/hard_124_binary-tree-maximum-path-sum.py
  - dfs/problems/medium_337_house-robber-iii.py
"""
from typing import List, Optional, Tuple


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    if not heights:
        return []
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()  # two independent passes' shared state

    def dfs(r, c, visited, prev_height):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if heights[r][c] < prev_height:
            return
        visited.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, visited, heights[r][c])

    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])

    # combine after both passes finish: cells reachable from both oceans.
    return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]


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


def test_pacific_atlantic():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    assert pacific_atlantic(heights) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]


def test_build_tree():
    tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert _to_list(tree) == [3, [9, None, None], [20, [15, None, None], [7, None, None]]]


def test_is_balanced():
    balanced = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(balanced) is True

    unbalanced = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert is_balanced(unbalanced) is False


if __name__ == "__main__":
    test_pacific_atlantic()
    test_build_tree()
    test_is_balanced()
    print("OK")
