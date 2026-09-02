"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference node in a connected undirected graph, return a deep
copy of the graph. Each node has a value and a list of neighbors.

Example:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
"""
from typing import Dict, List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None
    visited: Dict[Node, Node] = {}  # shared state: original -> clone

    def dfs(n):
        if n in visited:
            return visited[n]
        clone = Node(n.val)
        visited[n] = clone
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)


def _build(adj_list: List[List[int]]) -> Node:
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def _to_adj_list(node: Node) -> List[List[int]]:
    visited = {}

    def dfs(n):
        if n.val in visited:
            return
        visited[n.val] = sorted(neighbor.val for neighbor in n.neighbors)
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)
    return [visited[i + 1] for i in range(len(visited))]


def test_clone_graph():
    original = _build([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = clone_graph(original)
    assert cloned is not original
    assert _to_adj_list(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]


if __name__ == "__main__":
    test_clone_graph()
    print("OK")
