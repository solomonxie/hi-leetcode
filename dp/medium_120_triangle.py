"""
120. Triangle
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below - i.e.,
from index i you may move to index i or index i + 1 on the next row.

Example:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The path 2 -> 3 -> 5 -> 1 gives the minimum sum of 11.
"""
from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    dp = triangle[-1][:]
    for row in range(len(triangle) - 2, -1, -1):
        for i in range(len(triangle[row])):
            dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
    return dp[0]


def test_minimumTotal():
    assert minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11


if __name__ == "__main__":
    test_minimumTotal()
    print("OK")
