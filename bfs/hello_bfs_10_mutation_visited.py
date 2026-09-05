"""
Run: python3 hello_bfs_10_mutation_visited.py

Recap: step 3 used a separate `visited` set alongside the input.

Step 10: mark visited by mutation — when the input is mutable and
disposable (not needed in its original form afterward), mutate it in
place as the visited marker instead of allocating a separate set: flip
a grid's "1" to "0", overwrite a maze's "." with "+", recolor a pixel.
One fewer data structure, same guarantee — a position mutated this way
is never treated as unvisited again.

The mental model: "do I still need the original input after this
traversal?" If not, the input itself can double as `visited` — this
only works when overwriting a cell can't be confused with a value the
algorithm still needs to read.

Speedrun:
  - bfs/problems/medium_200_number-of-islands.py
  - bfs/problems/easy_733_flood-fill.py
  - bfs/problems/medium_1091_shortest-path-in-binary-matrix.py
  - bfs/problems/medium_1926_nearest-exit-from-entrance-in-maze.py
  - bfs/problems/medium_130_surrounded-regions.py
  - bfs/problems/medium_934_shortest-bridge.py
"""
from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                grid[r][c] = "0"   # the grid itself is the visited marker
                queue = deque([(r, c)])
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))
    return count


def test_num_islands():
    grid = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert num_islands(grid) == 1
    # no separate visited set — the grid was consumed instead.
    assert grid == [list("00000")] * 4


if __name__ == "__main__":
    test_num_islands()
    print("OK")
