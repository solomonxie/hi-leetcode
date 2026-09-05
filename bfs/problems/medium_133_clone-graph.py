"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference node in a connected undirected graph, return a deep
copy of the graph. Each node has a value and a list of neighbors.

Example:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
"""
from collections import deque
from typing import Dict, List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None
    clones: Dict[Node, Node] = {node: Node(node.val)}  # visited doubles as original -> clone
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        for neighbor in cur.neighbors:
            if neighbor not in clones:
                clones[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            clones[cur].neighbors.append(clones[neighbor])
    return clones[node]


def _build(adj_list: List[List[int]]) -> Node:
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def _to_adj_list(node: Node) -> List[List[int]]:
    visited = {}
    queue = deque([node])
    visited[node.val] = sorted(n.val for n in node.neighbors)
    while queue:
        cur = queue.popleft()
        for neighbor in cur.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = sorted(n.val for n in neighbor.neighbors)
                queue.append(neighbor)
    return [visited[i + 1] for i in range(len(visited))]


def test_clone_graph():
    original = _build([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = clone_graph(original)
    assert cloned is not original
    assert _to_adj_list(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]


if __name__ == "__main__":
    test_clone_graph()
    print("OK")
