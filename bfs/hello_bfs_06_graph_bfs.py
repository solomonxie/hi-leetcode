"""
Run: python3 hello_bfs_06_graph_bfs.py

Recap: step 5 generalized BFS from a tree to a grid, whose neighbors
came from a fixed offset rule.

Step 6: graph BFS — generalize once more, to an arbitrary graph given
as an adjacency list: `graph[node]` is just whatever nodes that node
connects to, with no geometry implied. A graph may also be
disconnected, so answering something about "every node" needs an outer
loop that starts a fresh BFS from every not-yet-visited node — each
such start is one connected component.

The mental model: a grid's neighbors are "the 4 adjacent cells"; a
graph's neighbors are "whatever `graph[node]` happens to list" — same
traversal, arbitrary edges instead of implied-by-geometry ones.

Speedrun:
  - bfs/problems/easy_1971_find-if-path-exists-in-graph.py
      Same shape as below, run directly on LeetCode's exact signature.
  - bfs/problems/medium_133_clone-graph.py
  - bfs/problems/medium_785_is-graph-bipartite.py
  - bfs/problems/medium_207_course-schedule.py
  - bfs/problems/medium_210_course-schedule-ii.py
  - bfs/problems/hard_127_word-ladder.py
"""
from collections import deque
from typing import List


def count_components(n: int, edges: List[List[int]]) -> int:
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def bfs(start):
        visited.add(start)
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    count = 0
    for node in range(n):
        if node not in visited:   # a fresh start = a new component
            count += 1
            bfs(node)
    return count


def test_count_components():
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


if __name__ == "__main__":
    test_count_components()
    print("OK")
