"""
Run: python3 hello_bfs_02_level_order.py

Recap: step 1 built a flat list of values in level order using a plain
FIFO queue and loop.

Step 2: level-order traversal — group step 1's flat output by level.
The trick: before draining any of the current level, snapshot
`len(queue)` — that's exactly how many nodes belong to this level,
since everything currently in the queue was pushed by the *previous*
level's processing, and nothing pushed *during* this level's
processing (i.e. the next level's nodes) is counted. Loop that many
times, and every push inside the loop is guaranteed to land in the
next level's batch.

The mental model: `len(queue)` at the top of the outer loop is a
snapshot, not a live value — it freezes "how many nodes are in the
current level" before the loop body mutates the queue.

Speedrun:
  - bfs/problems/medium_102_binary-tree-level-order-traversal.py
      Same shape as below, run directly on LeetCode's exact signature.
  - bfs/problems/medium_103_binary-tree-zigzag-level-order-traversal.py
  - bfs/problems/medium_429_n-ary-tree-level-order-traversal.py
  - bfs/problems/easy_637_average-of-levels-in-binary-tree.py
  - bfs/problems/medium_515_find-largest-value-in-each-tree-row.py
  - bfs/problems/medium_199_binary-tree-right-side-view.py
  - bfs/problems/medium_116_populating-next-right-pointers-in-each-node.py
  - bfs/problems/easy_111_minimum-depth-of-binary-tree.py
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)   # snapshot: freezes this level's node count
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def test_level_order():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(tree) == [[3], [9, 20], [15, 7]]


if __name__ == "__main__":
    test_level_order()
    print("OK")
