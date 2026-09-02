"""
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island bordering both the Pacific Ocean
(touching the top and left edges) and the Atlantic Ocean (touching the
bottom and right edges). heights[r][c] represents the height of the cell
at (r, c). Rain water can flow from a cell to an adjacent cell with
height less than or equal to its own, in the 4 cardinal directions.
Return a list of grid coordinates where water can flow to both the
Pacific and Atlantic oceans.

Example:
    Input: heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
    ]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
"""
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    if not heights:
        return []
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r, c, visited, prev_height):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prev_height:
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

    return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]


def test_pacificAtlantic():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    assert pacificAtlantic(heights) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]


if __name__ == "__main__":
    test_pacificAtlantic()
    print("OK")
