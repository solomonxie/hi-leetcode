"""
Run: python3 hello_dp_06_two_sequence_state.py

Recap: step 5's state was a position in *one* grid.

Step 6: two-sequence state — the state is a pair of indices into two
*different* sequences, `dp[i][j]` = "the answer using the first `i`
characters of word1 and the first `j` characters of word2." The
transition branches on whether the current characters match: a match
lets both indices advance for free (diagonal move); a mismatch has to
pay for an edit and try every way of advancing (delete/insert/replace).
The base cases are the edges of the table — one string exhausted, so the
answer is just however many characters remain in the other.

The mental model: draw an (m+1)-by-(n+1) grid where cell (i, j) means
"i chars of word1 done, j chars of word2 done," row 0 and column 0 are
the free-standing base cases, and every other cell reaches back to its
diagonal/up/left neighbor exactly like step 5 — just with the extra
"did these two characters match?" branch.

Speedrun:
  - dp/problems/hard_72_edit-distance.py
      dp[i][j] = min edits to turn word1[:i] into word2[:j].
"""


def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i  # delete all i chars of word1 to match empty word2
    for j in range(n + 1):
        dp[0][j] = j  # insert all j chars of word2 into empty word1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # match: free diagonal move
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete from word1
                    dp[i][j - 1],      # insert into word1
                    dp[i - 1][j - 1],  # replace
                )
    return dp[m][n]


def test_min_distance():
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "abc") == 3  # pure base-case row/column


if __name__ == "__main__":
    test_min_distance()
    print("OK")
