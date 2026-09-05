"""
863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Given the root of a binary tree, a target node, and an integer k,
return the values of all nodes that are exactly distance k from target.

Example:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
    Output: [7,4,1]
"""
from collections import deque
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distance_k(root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
    # a tree has no "parent" pointers, so build them once — this turns
    # the tree into an undirected graph BFS can spread through in every
    # direction, not just downward.
    parent: Dict[TreeNode, Optional[TreeNode]] = {}
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    visited = {target}
    queue = deque([target])
    dist = 0
    while queue:
        if dist == k:
            return [node.val for node in queue]
        dist += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbor in (node.left, node.right, parent.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return []


def _find(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return _find(root.left, val) or _find(root.right, val)


def test_distance_k():
    tree = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(0), TreeNode(8)),
    )
    target = _find(tree, 5)
    assert sorted(distance_k(tree, target, 2)) == [1, 4, 7]


if __name__ == "__main__":
    test_distance_k()
    print("OK")
