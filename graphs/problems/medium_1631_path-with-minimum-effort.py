"""
1631. Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort/

You are a hiker on an m x n grid of heights. You start at (0, 0) and
want to reach (rows-1, cols-1). The effort of a path is the maximum
absolute difference in heights between two consecutive cells along it.
Return the minimum effort required.

Example:
    Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2

    Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
"""
import heapq
from typing import List


def minimumEffortPath(heights: List[List[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    effort = [[float("inf")] * cols for _ in range(rows)]
    effort[0][0] = 0
    heap = [(0, 0, 0)]  # (max effort so far along the path, row, col)

    while heap:
        cur, r, c = heapq.heappop(heap)
        if (r, c) == (rows - 1, cols - 1):
            return cur
        if cur > effort[r][c]:
            continue
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                next_effort = max(cur, abs(heights[nr][nc] - heights[r][c]))
                if next_effort < effort[nr][nc]:
                    effort[nr][nc] = next_effort
                    heapq.heappush(heap, (next_effort, nr, nc))
    return 0


def test_minimumEffortPath():
    assert minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1


if __name__ == "__main__":
    test_minimumEffortPath()
    print("OK")
