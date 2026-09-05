"""
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/

You are given an m x n grid rooms where -1 is a wall, 0 is a gate, and
2^31-1 (INF) is an empty room. Fill each empty room with the distance
to its nearest gate, or leave it as INF if no gate can reach it.

Example:
    Input: rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
    Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""
from collections import deque
from typing import List

INF = 2**31 - 1


def walls_and_gates(rooms: List[List[int]]) -> None:
    if not rooms:
        return
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    # multi-source BFS: every gate starts the frontier at distance 0
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))


def test_walls_and_gates():
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    walls_and_gates(rooms)
    assert rooms == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]


if __name__ == "__main__":
    test_walls_and_gates()
    print("OK")
