"""
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Given an n-ary tree, return the level order traversal of its nodes'
values (i.e., from left to right, level by level).

Example:
    Input: root = [1,null,3,2,4,null,5,6]
    (1's children: 3, 2, 4; 3's children: 5, 6)
    Output: [[1],[3,2,4],[5,6]]
"""
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def level_order(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            for child in node.children:   # any number of children, not just two
                queue.append(child)
        result.append(level)
    return result


def test_level_order():
    tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    assert level_order(tree) == [[1], [3, 2, 4], [5, 6]]
    assert level_order(None) == []


if __name__ == "__main__":
    test_level_order()
    print("OK")
