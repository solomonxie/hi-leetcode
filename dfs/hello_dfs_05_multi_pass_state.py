"""
Run: python3 hello_dfs_05_multi_pass_state.py

Recap: step 4 shared one piece of state across an entire DFS traversal.

Step 5: independent state per pass — run DFS more than once, each pass
with its *own* fresh shared state (step 4's trick, repeated), then
combine the results afterward. The passes don't interfere because each
gets its own visited set; only the combining step (union/intersection)
ties them together.

The mental model: "can I answer this with one traversal whose state means
two things at once, or is it cleaner as two separate traversals with
simple state, combined at the end?" Usually the second is easier to reason
about correctly.

Speedrun:
  - dfs/problems/medium_417_pacific-atlantic-water-flow.py
      Two independent DFS sweeps — one seeded from the Pacific-facing
      border, one from the Atlantic-facing border — each with its own
      visited set, intersected at the end.
"""
from typing import List


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    if not heights:
        return []
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()  # two independent "shared state" sets

    def dfs(r, c, visited, prev_height):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if heights[r][c] < prev_height:
            return
        visited.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, visited, heights[r][c])

    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])

    # combine after both passes finish: cells reachable from both oceans.
    return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]


def test_pacific_atlantic():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    assert pacific_atlantic(heights) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]


if __name__ == "__main__":
    test_pacific_atlantic()
    print("OK")
