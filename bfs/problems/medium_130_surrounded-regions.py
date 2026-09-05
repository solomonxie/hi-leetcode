"""
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O', capture all regions
that are 4-directionally surrounded by 'X' by flipping their 'O's to
'X'. Regions connected to the border are not surrounded and stay 'O'.

Example:
    Input: board = [["X","X","X","X"],
                     ["X","O","O","X"],
                     ["X","X","O","X"],
                     ["X","O","X","X"]]
    Output:        [["X","X","X","X"],
                     ["X","X","X","X"],
                     ["X","X","X","X"],
                     ["X","O","X","X"]]
"""
from collections import deque
from typing import List


def solve(board: List[List[str]]) -> None:
    if not board:
        return
    rows, cols = len(board), len(board[0])
    queue = deque()

    # any 'O' on the border can never be surrounded — start BFS from all of them
    for r in range(rows):
        for c in (0, cols - 1):
            if board[r][c] == "O":
                queue.append((r, c))
                board[r][c] = "#"   # mark "safe" so it isn't flipped later
    for c in range(cols):
        for r in (0, rows - 1):
            if board[r][c] == "O":
                queue.append((r, c))
                board[r][c] = "#"

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                board[nr][nc] = "#"
                queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"    # surrounded: capture it
            elif board[r][c] == "#":
                board[r][c] = "O"    # border-connected: restore it


def test_solve():
    board = [
        list("XXXX"),
        list("XOOX"),
        list("XXOX"),
        list("XOXX"),
    ]
    solve(board)
    assert board == [
        list("XXXX"),
        list("XXXX"),
        list("XXXX"),
        list("XOXX"),
    ]


if __name__ == "__main__":
    test_solve()
    print("OK")
