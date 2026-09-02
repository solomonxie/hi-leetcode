"""
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition
is a palindrome. Return all possible palindrome partitionings of s.

Example:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
"""
from typing import List


def partition(s: str) -> List[List[str]]:
    result = []
    path = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if not is_palindrome(piece):
                continue
            path.append(piece)
            backtrack(end)
            path.pop()

    backtrack(0)
    return result


def test_partition():
    result = partition("aab")
    assert sorted(map(tuple, result)) == sorted(map(tuple, [["a", "a", "b"], ["aa", "b"]]))


if __name__ == "__main__":
    test_partition()
    print("OK")
