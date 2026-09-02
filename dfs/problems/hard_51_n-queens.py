"""
51. N-Queens
https://leetcode.com/problems/n-queens/

Place n queens on an n x n chessboard such that no two queens attack
each other. Return all distinct board configurations, each as a list of
strings using 'Q' and '.'.

Example:
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
"""
from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    result = []
    cols, diag, anti_diag = set(), set(), set()
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag or (row + col) in anti_diag:
                continue
            cols.add(col); diag.add(row - col); anti_diag.add(row + col)
            board[row][col] = "Q"

            backtrack(row + 1)

            board[row][col] = "."
            cols.remove(col); diag.remove(row - col); anti_diag.remove(row + col)

    backtrack(0)
    return result


def test_solve_n_queens():
    result = solve_n_queens(4)
    assert sorted(map(tuple, result)) == sorted(
        map(tuple, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    )


if __name__ == "__main__":
    test_solve_n_queens()
    print("OK")
