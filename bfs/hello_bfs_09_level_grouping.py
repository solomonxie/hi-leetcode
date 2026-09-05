"""
Run: python3 hello_bfs_09_level_grouping.py

Recap: step 2 introduced the `len(queue)` snapshot to know where one
level ends; every step since then flattened that away into a single
running value (distance, steps).

Step 9: level grouping — put the snapshot back to work for problems
that need a *fact per level*, not a single final number: every value on
this level, the max on this level, the last one seen on this level. The
snapshot technique from step 2 is the same; what changes is what gets
computed from `level` before moving to the next iteration.

The mental model: level-order traversal (step 2) and distance tracking
(step 4) are two ends of the same technique — grouping by level is
what step 2 was already doing; step 4 just discarded the grouping and
kept a running counter instead.

Speedrun:
  - bfs/problems/medium_102_binary-tree-level-order-traversal.py
  - bfs/problems/medium_103_binary-tree-zigzag-level-order-traversal.py
  - bfs/problems/medium_429_n-ary-tree-level-order-traversal.py
  - bfs/problems/easy_637_average-of-levels-in-binary-tree.py
  - bfs/problems/medium_515_find-largest-value-in-each-tree-row.py
  - bfs/problems/medium_199_binary-tree-right-side-view.py
  - bfs/problems/medium_116_populating-next-right-pointers-in-each-node.py
  - bfs/problems/medium_863_all-nodes-distance-k-in-binary-tree.py
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:    # last one drained this level = rightmost
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


def test_right_side_view():
    tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(tree) == [1, 3, 4]


if __name__ == "__main__":
    test_right_side_view()
    print("OK")
