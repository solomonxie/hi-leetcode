"""
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square numbers
(1, 4, 9, 16, ...) that sum to n.

Example:
    Input: n = 12
    Output: 3   (4 + 4 + 4)

    Input: n = 13
    Output: 2   (4 + 9)
"""
from collections import deque


def num_squares(n: int) -> int:
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    # BFS over remainders: each state is "how much is left to reach 0,"
    # and each edge subtracts one perfect square — the first time we hit
    # 0 is via the fewest such subtractions.
    visited = {n}
    queue = deque([(n, 0)])
    while queue:
        remainder, steps = queue.popleft()
        if remainder == 0:
            return steps
        for square in squares:
            if square > remainder:
                break
            next_remainder = remainder - square
            if next_remainder not in visited:
                visited.add(next_remainder)
                queue.append((next_remainder, steps + 1))
    return -1


def test_num_squares():
    assert num_squares(12) == 3
    assert num_squares(13) == 2
    assert num_squares(1) == 1


if __name__ == "__main__":
    test_num_squares()
    print("OK")
