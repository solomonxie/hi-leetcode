"""
72. Edit Distance
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2. You have three operations permitted
on a word: insert a character, delete a character, or replace a character.

Example:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: horse -> rorse (replace 'h' with 'r')
                 rorse -> rose (remove 'r')
                 rose -> ros (remove 'e')

    Input: word1 = "intention", word2 = "execution"
    Output: 5
"""


def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1],
                )
    return dp[m][n]


def test_minDistance():
    assert minDistance("horse", "ros") == 3
    assert minDistance("intention", "execution") == 5


if __name__ == "__main__":
    test_minDistance()
    print("OK")
