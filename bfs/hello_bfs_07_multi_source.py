"""
Run: python3 hello_bfs_07_multi_source.py

Recap: step 6 always started BFS from one node (or one node per
component, taken one at a time).

Step 7: multi-source BFS — push every starting position at once, all at
distance 0, instead of one. The queue then expands outward from all of
them simultaneously, and the first time BFS reaches a cell, it's
necessarily via the *nearest* of the sources — no need to run a
separate single-source BFS per source and take the minimum.

The mental model: "distance from the nearest of several starting
points" is one BFS, not several — seed the queue with all sources up
front, all sharing distance 0, and let normal BFS take over.

Speedrun:
  - bfs/problems/medium_994_rotting-oranges.py
      Every initially-rotten orange is a source pushed at minute 0.
  - bfs/problems/medium_542_01-matrix.py
  - bfs/problems/medium_286_walls-and-gates.py
  - bfs/problems/medium_934_shortest-bridge.py
  - bfs/problems/medium_130_surrounded-regions.py
      Every border 'O' is a source — none of them can be surrounded.
"""
from collections import deque
from typing import List


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    rows, cols = len(mat), len(mat[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    for r in range(rows):          # seed every 0 cell at once, all at distance 0
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist


def test_update_matrix():
    assert update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]


if __name__ == "__main__":
    test_update_matrix()
    print("OK")
