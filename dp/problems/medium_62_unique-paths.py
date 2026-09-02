"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of an m x n grid. The robot can
only move either down or right at any point in time, trying to reach the
bottom-right corner. How many possible unique paths are there?

Example:
    Input: m = 3, n = 7
    Output: 28

    Input: m = 3, n = 2
    Output: 3
    Explanation: Right->Down->Down, Down->Right->Down, Down->Down->Right.
"""


def uniquePaths(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


def test_uniquePaths():
    assert uniquePaths(3, 7) == 28
    assert uniquePaths(3, 2) == 3


if __name__ == "__main__":
    test_uniquePaths()
    print("OK")
