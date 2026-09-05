"""
1392. Longest Happy Prefix
https://leetcode.com/problems/longest-happy-prefix/

A "happy prefix" is a non-empty prefix of s that is also a suffix of s
(excluding s itself). Return the longest happy prefix, or "" if none
exists.

Example:
    Input: s = "level"
    Output: "l"

    Input: s = "ababab"
    Output: "abab"
"""


def longestPrefix(s: str) -> str:
    # This is exactly KMP's lps array computed on s against itself:
    # lps[-1] is the length of the longest proper prefix of s that is
    # also a suffix of s — a "happy prefix" by definition.
    lps = [0] * len(s)
    length = 0
    i = 1
    while i < len(s):
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return s[: lps[-1]] if s else ""


def test_longestPrefix():
    assert longestPrefix("level") == "l"
    assert longestPrefix("ababab") == "abab"
    assert longestPrefix("leetcodeleet") == "leet"
    assert longestPrefix("a") == ""


if __name__ == "__main__":
    test_longestPrefix()
    print("OK")
