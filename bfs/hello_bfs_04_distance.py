"""
Run: python3 hello_bfs_04_distance.py

Recap: step 3 added a visited set to stop BFS from enqueuing the same
position twice.

Step 4: distance / step counting — BFS visits positions in strictly
non-decreasing distance from the start, because everything one step
away is pushed (and therefore popped) before anything two steps away.
That guarantee is what makes BFS *the* algorithm for "fewest steps" /
"shortest path" on an unweighted graph: the first time you reach a
target, it's necessarily via the fewest possible edges — track the
distance alongside each position and stop as soon as you hit it.

The mental model: "distance so far" is state carried per queue entry
(a `(position, distance)` pair, or a parallel counter), not something
computed after the fact — each push is exactly one step farther than
the node that pushed it.

Speedrun:
  - bfs/problems/easy_111_minimum-depth-of-binary-tree.py
      Same idea as below, on a tree instead of a grid: the first leaf
      reached is necessarily the shallowest one.
  - bfs/problems/medium_1091_shortest-path-in-binary-matrix.py
  - bfs/problems/medium_1926_nearest-exit-from-entrance-in-maze.py
  - bfs/problems/medium_279_perfect-squares.py
  - bfs/problems/medium_752_open-the-lock.py
  - bfs/problems/hard_127_word-ladder.py
  - bfs/problems/medium_542_01-matrix.py
  - bfs/problems/medium_994_rotting-oranges.py
  - bfs/problems/medium_863_all-nodes-distance-k-in-binary-tree.py
  - bfs/problems/medium_934_shortest-bridge.py
"""
from collections import deque
from typing import List


def shortest_path_length(grid: List[List[int]]) -> int:
    # 0 = open, 1 = wall. Shortest number of steps from top-left to
    # bottom-right, 4-directionally, or -1 if unreachable.
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    visited = {(0, 0)}
    queue = deque([(0, 0, 0)])   # (row, col, distance) — distance rides along
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1


def test_shortest_path_length():
    assert shortest_path_length([[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 4
    assert shortest_path_length([[0, 1], [1, 0]]) == -1


if __name__ == "__main__":
    test_shortest_path_length()
    print("OK")
