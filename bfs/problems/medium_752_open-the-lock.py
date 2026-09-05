"""
752. Open the Lock
https://leetcode.com/problems/open-the-lock/

A lock has 4 dials, each 0-9, starting at "0000". One move turns one
dial one step. Given deadends (combinations that lock the wheel forever)
and a target, return the minimum number of moves to reach target, or -1
if impossible.

Example:
    Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
    Output: 6
"""
from collections import deque
from typing import List


def open_lock(deadends: List[str], target: str) -> int:
    dead = set(deadends)
    start = "0000"
    if start in dead:
        return -1
    if start == target:
        return 0

    def neighbors(state):
        for i in range(4):
            digit = int(state[i])
            for delta in (1, -1):
                new_digit = (digit + delta) % 10
                yield state[:i] + str(new_digit) + state[i + 1:]

    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        state, turns = queue.popleft()
        for nxt in neighbors(state):
            if nxt == target:
                return turns + 1
            if nxt not in visited and nxt not in dead:
                visited.add(nxt)
                queue.append((nxt, turns + 1))
    return -1


def test_open_lock():
    assert open_lock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert open_lock(["8888"], "0009") == 1
    assert open_lock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1


if __name__ == "__main__":
    test_open_lock()
    print("OK")
