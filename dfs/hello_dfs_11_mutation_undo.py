"""
Run: python3 hello_dfs_11_mutation_undo.py

Recap: step 8/9 marked positions visited and left them marked forever;
step 10 mutated a `path` list and undid the mutation before the next
choice.

Step 11: mutation + undo — apply step 10's undo discipline to the input
structure itself, not just a separate `path`. Mark a cell visited by
mutating it in place, recurse, then restore its original value before
returning — because unlike step 8/9's permanent visited set, a *different*
starting path may legitimately need to pass through this same cell again.

The mental model: "does 'visited' mean forever (step 8/9: one traversal,
each cell used once total) or just 'currently on this path' (step 11:
many attempted paths, each cell reusable once its path retreats)?"

Speedrun:
  - dfs/problems/medium_79_word-search.py
      Same shape as below, run directly on LeetCode's exact signature.
  - dfs/problems/hard_51_n-queens.py
  - dfs/problems/medium_46_permutations.py
  - dfs/problems/medium_78_subsets.py
  - dfs/problems/medium_90_subsets-ii.py
  - dfs/problems/medium_47_permutations-ii.py
  - dfs/problems/medium_131_palindrome-partitioning.py
  - dfs/problems/medium_22_generate-parentheses.py
  - dfs/problems/medium_39_combination-sum.py
  - dfs/problems/medium_17_letter-combinations-of-a-phone-number.py
"""
from typing import List


def exists(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False

        original, board[r][c] = board[r][c], "#"   # mutate: mark visited for this path
        found = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        board[r][c] = original                      # undo: a different path may need this cell

        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


def test_exists():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exists(board, "ABCCED") is True
    assert exists(board, "SEE") is True
    assert exists(board, "ABCB") is False
    # board is fully restored after every attempted path, successful or not.
    assert board == [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


if __name__ == "__main__":
    test_exists()
    print("OK")
