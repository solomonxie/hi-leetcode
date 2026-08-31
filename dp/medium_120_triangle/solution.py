# https://leetcode.com/problems/triangle/
from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    dp = triangle[-1][:]  # start from the bottom row
    for row in range(len(triangle) - 2, -1, -1):
        for i in range(len(triangle[row])):
            dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
    return dp[0]


if __name__ == "__main__":
    print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
