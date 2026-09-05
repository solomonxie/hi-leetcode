"""
116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Given a perfect binary tree, populate each node's next pointer to point
to its next right node. If there is no next right node, the next
pointer should be set to None.

Example:
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]  (# marks the end of each level)
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return root
    queue = deque([root])
    while queue:
        prev = None
        for _ in range(len(queue)):
            node = queue.popleft()
            if prev:
                prev.next = node   # link the previous node in this level to this one
            prev = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


def _next_chain(node: Optional[Node]):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals


def test_connect():
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    connect(root)
    assert _next_chain(root) == [1]
    assert _next_chain(root.left) == [2, 3]
    assert _next_chain(root.left.left) == [4, 5, 6, 7]


if __name__ == "__main__":
    test_connect()
    print("OK")
