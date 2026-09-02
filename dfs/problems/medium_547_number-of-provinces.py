"""
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/

There are n cities. isConnected[i][j] = 1 if city i and city j are
directly connected, 0 otherwise. A province is a group of directly or
indirectly connected cities. Return the total number of provinces.

Example:
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
"""
from typing import List


def find_circle_num(is_connected: List[List[int]]) -> int:
    n = len(is_connected)
    visited = set()

    def dfs(city):
        visited.add(city)
        for neighbor in range(n):
            if is_connected[city][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    count = 0
    for city in range(n):
        if city not in visited:
            count += 1
            dfs(city)
    return count


def test_find_circle_num():
    assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert find_circle_num([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3


if __name__ == "__main__":
    test_find_circle_num()
    print("OK")
