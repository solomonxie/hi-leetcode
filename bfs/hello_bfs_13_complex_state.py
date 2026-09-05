"""
Run: python3 hello_bfs_13_complex_state.py

Recap: every step so far has been one technique in isolation — level
grouping, visited, multi-source, mutation, queue state. Real problems
combine them.

Step 13: complex state — one traversal doing two things at once.
Shortest Bridge is a clean example: phase one floods the first island
(marking it, not BFS yet) and collects its cells as a *set of sources*;
phase two is a multi-source BFS (step 7) outward from that whole
island, with distance tracking (step 4) and mutation-as-visited
(step 10), stopping the instant it touches the second island. Three
techniques, one traversal, because splitting them into fully separate
passes would mean re-deriving the same visited state twice.

The mental model: "can this be one BFS whose queue seeds and per-step
state carry both facts I need, or is it clearer as two separate BFS
passes combined at the end?" Both are legitimate — Shortest Bridge
below picks the first; Walls and Gates (step 7) implicitly picks the
same one-pass shape for a simpler reason (only one kind of source).

Speedrun:
  - bfs/problems/medium_934_shortest-bridge.py
      Flood the first island, then multi-source BFS from its whole
      border to the second — mutation, multi-source and distance
      tracking in one pass.
  - bfs/problems/medium_863_all-nodes-distance-k-in-binary-tree.py
      A one-time parent-pointer pass turns a tree into an undirected
      graph, then plain BFS (step 6) spreads through it in every
      direction, not just downward.
  - bfs/problems/medium_130_surrounded-regions.py
  - bfs/problems/medium_994_rotting-oranges.py
  - bfs/problems/medium_542_01-matrix.py
  - bfs/problems/medium_286_walls-and-gates.py
"""
from collections import deque
from typing import List, Tuple


def shortest_bridge(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def neighbors(r, c):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    def find_first_island() -> Tuple[int, int]:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return r, c
        raise ValueError("no island found")

    # phase 1: flood the first island (mutation-as-visited, step 10),
    # collecting its cells as the multi-source frontier for phase 2.
    start = find_first_island()
    stack = [start]
    grid[start[0]][start[1]] = 2
    island = deque([start])
    while stack:
        r, c = stack.pop()
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                grid[nr][nc] = 2
                stack.append((nr, nc))
                island.append((nr, nc))

    # phase 2: multi-source BFS (step 7) carrying distance state
    # (step 4), still mutating as it goes (step 10).
    queue = deque((r, c, 0) for r, c in island)
    while queue:
        r, c, dist = queue.popleft()
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                return dist
            if grid[nr][nc] == 0:
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))
    return -1


def test_shortest_bridge():
    assert shortest_bridge([[0, 1], [1, 0]]) == 1
    assert shortest_bridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2


if __name__ == "__main__":
    test_shortest_bridge()
    print("OK")
