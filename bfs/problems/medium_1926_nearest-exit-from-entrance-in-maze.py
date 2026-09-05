"""
1926. Nearest Exit from Entrance in Maze
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

Given an m x n maze of '.' (empty) and '+' (wall) cells and an entrance,
return the shortest number of steps to reach any exit (an empty border
cell other than the entrance itself). Return -1 if no exit is
reachable.

Example:
    Input: maze = [["+","+",".","+"],
                    [".",".",".","+"],
                    ["+","+","+","."]], entrance = [1,2]
    Output: 1
"""
from collections import deque
from typing import List


def nearest_exit(maze: List[List[str]], entrance: List[int]) -> int:
    rows, cols = len(maze), len(maze[0])
    sr, sc = entrance
    queue = deque([(sr, sc, 0)])
    maze[sr][sc] = "+"   # mark visited by mutating in place

    while queue:
        r, c, steps = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                    return steps + 1
                maze[nr][nc] = "+"
                queue.append((nr, nc, steps + 1))
    return -1


def test_nearest_exit():
    maze = [
        list("++.+"),
        list("...+"),
        list("+++."),
    ]
    assert nearest_exit(maze, [1, 2]) == 1

    maze2 = [list(".+")]
    assert nearest_exit(maze2, [0, 0]) == -1


if __name__ == "__main__":
    test_nearest_exit()
    print("OK")
