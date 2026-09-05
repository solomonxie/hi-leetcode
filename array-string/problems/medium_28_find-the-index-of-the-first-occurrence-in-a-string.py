"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of
haystack.

Example:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
"""
from typing import List


def _build_lps(pattern: str) -> List[int]:
    # lps[i] = length of the longest proper prefix of pattern[:i+1] that
    # is also a suffix of it — how far to fall back on a mismatch instead
    # of restarting the haystack scan from scratch.
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    lps = _build_lps(needle)
    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                return i - j
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    return -1


def test_strStr():
    assert strStr("sadbutsad", "sad") == 0
    assert strStr("leetcode", "leeto") == -1
    assert strStr("aaaaa", "bba") == -1
    assert strStr("mississippi", "issip") == 4


if __name__ == "__main__":
    test_strStr()
    print("OK")
