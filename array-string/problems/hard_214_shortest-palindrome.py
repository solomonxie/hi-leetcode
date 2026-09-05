"""
214. Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/

Given a string s, convert it to a palindrome by adding characters in
front of it. Return the shortest palindrome you can find by doing this.

Example:
    Input: s = "aacecaaa"
    Output: "aaacecaaa"

    Input: s = "abcd"
    Output: "dcbabcd"
"""
from typing import List


def _build_lps(pattern: str) -> List[int]:
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


def shortestPalindrome(s: str) -> str:
    if not s:
        return s
    # '#' separates s from its reverse so the KMP match can never cross
    # past the true midpoint. The last lps value is then the length of
    # the longest prefix of s that already reads as a palindrome.
    combined = s + "#" + s[::-1]
    lps = _build_lps(combined)
    longest_palindromic_prefix = lps[-1]
    remainder = s[longest_palindromic_prefix:]
    return remainder[::-1] + s


def test_shortestPalindrome():
    assert shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert shortestPalindrome("abcd") == "dcbabcd"
    assert shortestPalindrome("") == ""
    assert shortestPalindrome("a") == "a"


if __name__ == "__main__":
    test_shortestPalindrome()
    print("OK")
