"""
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given an m x n board containing 'X' and 'O', capture all regions of 'O'
that are 4-directionally surrounded by 'X' by flipping them to 'X'.
Regions connected to the border are not captured.

Example:
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
"""
from typing import List


def solve(board: List[List[str]]) -> None:
    if not board:
        return
    rows, cols = len(board), len(board[0])
    safe = set()  # cells connected to the border — visited, but never captured

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in safe or board[r][c] != "O":
            return
        safe.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O" and (r, c) not in safe:
                board[r][c] = "X"


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
