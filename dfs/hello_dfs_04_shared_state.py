"""
Run: python3 hello_dfs_04_shared_state.py

Recap: step 1 returned values up, step 2 pushed context down, step 3
threaded a mutating `path` through choose/un-choose calls.

Step 4: shared state across calls — sometimes what you need isn't
naturally a return value or a passed-down parameter, it's one object
every call reads and mutates *directly*: a visited set, a counter, or
the input structure itself (mark-in-place). Python closures let an inner
dfs() reach outer variables; `nonlocal` is needed to reassign one
(mutating a list/set/dict in place doesn't need it — only rebinding does).

The mental model: "is this state really per-branch (step 2/3), or is it
one running total the whole traversal shares?" Visited-tracking and
counting are almost always shared state, not per-branch state.

Speedrun (dfs/problems/):
  - medium_200_number-of-islands.py
      The grid itself is the shared state — dfs() marks a cell visited
      by flipping it to "0" in place, so no separate visited set is needed.
  - medium_230_kth-smallest-element-in-a-bst.py
      A shared counter (`nonlocal`) ticks down across recursive calls,
      and the traversal exits early the moment it hits zero.
"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"  # shared state: the grid, mutated in place as "visited"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


def count_leaves(node) -> int:
    """A `nonlocal` counter: shared state that isn't the tree itself."""
    total = 0

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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_num_islands():
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(grid) == 3


def test_count_leaves():
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert count_leaves(tree) == 3


if __name__ == "__main__":
    test_num_islands()
    test_count_leaves()
    print("OK")
