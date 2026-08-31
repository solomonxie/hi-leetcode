"""
Run: python3 hello_topological_sorting.py

Topological sort orders the nodes of a Directed Acyclic Graph (DAG) so that
for every edge u -> v, u appears before v. It only makes sense on a DAG: a
cycle means there's no valid order (you'd need to schedule something before
itself). Classic uses: course prerequisites, build/task dependency graphs,
package install order.

Two standard ways to compute it:
  1. Kahn's algorithm (BFS): repeatedly peel off nodes with in-degree 0.
  2. DFS post-order: run DFS, append each node when it finishes, reverse.
"""

from collections import deque, defaultdict


def topological_sort_kahn(graph):
    """BFS approach. graph: {node: [neighbors]}. Returns [] if a cycle exists."""
    in_degree = defaultdict(int)
    for node in graph:
        in_degree.setdefault(node, 0)
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # start from every node with no incoming edges
    queue = deque(node for node, deg in in_degree.items() if deg == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # if we couldn't place every node, the graph has a cycle
    if len(order) != len(in_degree):
        return []
    return order


def topological_sort_dfs(graph):
    """DFS approach. Returns [] if a cycle exists."""
    WHITE, GRAY, BLACK = 0, 1, 2  # unvisited, on current path, done
    state = defaultdict(int)
    order = []
    has_cycle = False

    def visit(node):
        nonlocal has_cycle
        state[node] = GRAY
        for neighbor in graph.get(node, []):
            if state[neighbor] == GRAY:
                has_cycle = True  # back edge -> cycle
                return
            if state[neighbor] == WHITE:
                visit(neighbor)
        state[node] = BLACK
        order.append(node)  # append on finish -> post-order

    for node in graph:
        if state[node] == WHITE:
            visit(node)

    if has_cycle:
        return []
    return order[::-1]  # reverse post-order = topological order


if __name__ == "__main__":
    # e.g. "b depends on a" is drawn as an edge a -> b
    courses = {
        "intro": ["data-structures", "discrete-math"],
        "discrete-math": ["algorithms"],
        "data-structures": ["algorithms"],
        "algorithms": ["capstone"],
        "capstone": [],
    }

    print("Kahn's algorithm:", topological_sort_kahn(courses))
    print("DFS post-order:  ", topological_sort_dfs(courses))

    cyclic = {"a": ["b"], "b": ["c"], "c": ["a"]}
    print("Cyclic graph (no valid order):", topological_sort_kahn(cyclic))
