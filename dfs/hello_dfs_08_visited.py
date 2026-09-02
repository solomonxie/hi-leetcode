"""
Run: python3 hello_dfs_08_visited.py

Recap: step 7 was one shared object every call reads and mutates.

Step 8: visited — a specific, very common use of shared state (step 7):
a set that records which positions a traversal has already been to, so
it never revisits one and loops forever. Trees never needed this (a
node has exactly one path down from the root, so there's nothing to
loop back to) — grids and graphs do, since a cell/node can be reached
from more than one direction.

The mental model: "could this traversal ever reach the same position
twice?" If yes, `visited` isn't optional — without it, DFS on a grid or
graph can recurse forever between two cells that are each other's
neighbor.

Speedrun:
  - dfs/problems/medium_200_number-of-islands.py
      A different visited technique: instead of a separate set, it
      mutates the grid itself ("1" -> "0") as the visited marker.
  - dfs/problems/medium_417_pacific-atlantic-water-flow.py
  - dfs/problems/medium_79_word-search.py
  - dfs/problems/medium_130_surrounded-regions.py
  - dfs/problems/easy_1971_find-if-path-exists-in-graph.py
  - dfs/problems/medium_547_number-of-provinces.py
  - dfs/problems/medium_323_number-of-connected-components-in-an-undirected-graph.py
  - dfs/problems/medium_133_clone-graph.py
  - dfs/problems/medium_1448_count-good-nodes-in-binary-tree.py
  - dfs/problems/medium_207_course-schedule.py
"""
from typing import List, Set, Tuple


def count_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited: Set[Tuple[int, int]] = set()  # explicit shared state, not the grid itself

    def dfs(r, c):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                dfs(r, c)
    return count


def test_count_islands():
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert count_islands(grid) == 3
    # grid is untouched — the visited set carried the state, not the input.
    assert grid[0][0] == "1"


if __name__ == "__main__":
    test_count_islands()
    print("OK")
