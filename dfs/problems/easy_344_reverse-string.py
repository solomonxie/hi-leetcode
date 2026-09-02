"""
344. Reverse String
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as
an array of characters s, and it must be modified in place.

Example:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    def dfs(lo, hi):
        if lo >= hi:
            return
        s[lo], s[hi] = s[hi], s[lo]
        dfs(lo + 1, hi - 1)

    dfs(0, len(s) - 1)


def test_reverse_string():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]


if __name__ == "__main__":
    test_reverse_string()
    print("OK")
