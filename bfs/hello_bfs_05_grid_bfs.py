"""
Run: python3 hello_bfs_05_grid_bfs.py

Recap: step 3's visited set and step 4's distance tracking both ran on
a grid already, but only informally — this step names the shape.

Step 5: grid BFS — a grid is a graph in disguise: each cell's
"neighbors" are its (up to 4) adjacent cells, generated from a fixed
offset list instead of looked up in an adjacency list. Everything else
— queue, visited, distance — is exactly steps 1-4, just applied to
`(row, col)` tuples instead of tree nodes.

The mental model: whenever a problem gives a 2D grid and asks about
"reachable," "shortest," or "connected," picture the grid's cells as
graph nodes and its 4-neighbor rule as the edge list — the traversal
code barely changes from a tree/graph version.

Speedrun:
  - bfs/problems/medium_200_number-of-islands.py
  - bfs/problems/medium_1091_shortest-path-in-binary-matrix.py
  - bfs/problems/medium_1926_nearest-exit-from-entrance-in-maze.py
  - bfs/problems/medium_542_01-matrix.py
  - bfs/problems/medium_130_surrounded-regions.py
  - bfs/problems/easy_733_flood-fill.py
  - bfs/problems/medium_994_rotting-oranges.py
  - bfs/problems/medium_934_shortest-bridge.py
  - bfs/problems/medium_286_walls-and-gates.py
"""
from collections import deque
from typing import List

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))  # the "neighbors" of a grid cell


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start_color = image[sr][sc]
    if start_color == color:
        return image
    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color
    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                image[nr][nc] = color
                queue.append((nr, nc))
    return image


def test_flood_fill():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert flood_fill(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


if __name__ == "__main__":
    test_flood_fill()
    print("OK")
