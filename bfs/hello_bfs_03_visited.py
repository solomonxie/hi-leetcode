"""
Run: python3 hello_bfs_03_visited.py

Recap: step 2's level batching never worried about revisiting a node —
a tree has exactly one path down from the root, so there's nothing to
loop back to.

Step 3: visited — grids and general graphs can reach the same position
from more than one direction, so BFS needs an explicit set of positions
already seen. Mark a position visited the moment it's *pushed*, not
when it's popped — otherwise the same position can be pushed multiple
times before it's ever processed, wasting work (or, on some problems,
producing wrong answers by counting/visiting it more than once).

The mental model: "could this traversal ever reach the same position
twice?" If yes, visited isn't optional — without it, BFS on a grid or
graph enqueues duplicates forever between cells that are each other's
neighbor.

Speedrun:
  - bfs/problems/medium_200_number-of-islands.py
      A different visited technique: instead of a separate set, it
      mutates the grid itself ("1" -> "0") as the visited marker.
  - bfs/problems/easy_1971_find-if-path-exists-in-graph.py
  - bfs/problems/medium_133_clone-graph.py
  - bfs/problems/medium_785_is-graph-bipartite.py
  - bfs/problems/medium_207_course-schedule.py
  - bfs/problems/medium_130_surrounded-regions.py
  - bfs/problems/medium_1091_shortest-path-in-binary-matrix.py
  - bfs/problems/medium_1926_nearest-exit-from-entrance-in-maze.py
  - bfs/problems/medium_934_shortest-bridge.py
  - bfs/problems/medium_542_01-matrix.py
"""
from collections import deque
from typing import List, Set, Tuple


def count_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited: Set[Tuple[int, int]] = set()  # explicit shared state, not the grid itself

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))   # mark on push
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == "1" and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))   # mark before pushing, not after popping
                    queue.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                bfs(r, c)
    return count


def test_count_islands():
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert count_islands(grid) == 3
    # grid is untouched — the visited set carried the state, not the input.
    assert grid[0][0] == "1"


if __name__ == "__main__":
    test_count_islands()
    print("OK")
