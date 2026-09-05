"""
Run: python3 hello_bfs_01_queue.py

Step 1: queue — the primitive BFS runs on. A queue is FIFO (first in,
first out): whatever was pushed earliest comes out first. That's the
opposite of the call stack DFS uses (LIFO — last in, first out), and
it's why BFS explores breadth-first instead of depth-first: everything
one step away gets visited before anything two steps away, because it
was pushed to the queue first.

Python's list has O(n) pop(0); collections.deque gives O(1) append and
popleft, so BFS always uses a deque, never a plain list, as its queue.

The mental model: push starting points in, then loop "pop the front,
look at it, push whatever's next" until the queue is empty. Nothing
about *what* you're traversing (a tree, a grid, a graph) matters yet —
just the FIFO discipline.

Speedrun (trace the order values come out, not what they mean yet):
  - bfs/problems/easy_637_average-of-levels-in-binary-tree.py
  - bfs/problems/medium_515_find-largest-value-in-each-tree-row.py
  - bfs/problems/easy_111_minimum-depth-of-binary-tree.py
  - bfs/problems/medium_199_binary-tree-right-side-view.py
  - bfs/problems/medium_429_n-ary-tree-level-order-traversal.py
  - bfs/problems/easy_733_flood-fill.py
  - bfs/problems/easy_1971_find-if-path-exists-in-graph.py
  - bfs/problems/medium_200_number-of-islands.py
  - bfs/problems/medium_116_populating-next-right-pointers-in-each-node.py
  - bfs/problems/medium_102_binary-tree-level-order-traversal.py
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fifo_order(items: List[int]) -> List[int]:
    # push everything, then drain it — output order equals input order.
    queue = deque()
    for item in items:
        queue.append(item)
    order = []
    while queue:
        order.append(queue.popleft())
    return order


def bfs_values(root: Optional[TreeNode]) -> List[int]:
    # push root, then repeatedly pop the front and push its children —
    # values come out in level order simply because FIFO guarantees it.
    if root is None:
        return []
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def test_fifo_order():
    assert fifo_order([1, 2, 3]) == [1, 2, 3]


def test_bfs_values():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert bfs_values(tree) == [3, 9, 20, 15, 7]


if __name__ == "__main__":
    test_fifo_order()
    test_bfs_values()
    print("OK")
