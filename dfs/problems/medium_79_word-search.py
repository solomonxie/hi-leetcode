"""
79. Word Search
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if
word exists in the grid. The word can be constructed from letters of
sequentially adjacent cells (horizontally or vertically neighboring); the
same cell may not be used more than once in one word.

Example:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
           word = "ABCCED"
    Output: true

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
           word = "SEE"
    Output: true
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False

        board[r][c] = "#"  # mark visited for this path
        found = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        board[r][c] = word[i]  # undo: a different path may need this cell

        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


def test_exist():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED") is True
    assert exist(board, "SEE") is True
    assert exist(board, "ABCB") is False


if __name__ == "__main__":
    test_exist()
    print("OK")
