"""
934. Shortest Bridge
https://leetcode.com/problems/shortest-bridge/

Given a grid with exactly two islands of 1s (connected 4-directionally),
return the minimum number of 0s you must flip to connect them into one
island.

Example:
    Input: grid = [[0,1],[1,0]]
    Output: 1
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

    # phase 1: DFS/flood the first island, marking it and collecting its
    # border cells as the multi-source frontier for phase 2.
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

    # phase 2: multi-source BFS outward from the whole first island until
    # a cell belonging to the second island (still marked 1) is reached.
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
    assert shortest_bridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 1


if __name__ == "__main__":
    test_shortest_bridge()
    print("OK")
