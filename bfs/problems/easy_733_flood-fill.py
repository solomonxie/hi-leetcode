"""
733. Flood Fill
https://leetcode.com/problems/flood-fill/

You are given an image, a starting pixel (sr, sc), and a color. Perform
a flood fill: change the starting pixel's color and every pixel
connected to it (4-directionally, same original color) to the new
color.

Example:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
"""
from collections import deque
from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start_color = image[sr][sc]
    if start_color == color:
        return image
    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color   # mark visited by mutating in place

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                image[nr][nc] = color
                queue.append((nr, nc))
    return image


def test_flood_fill():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert flood_fill(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


if __name__ == "__main__":
    test_flood_fill()
    print("OK")
