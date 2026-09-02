"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent, using the standard
phone keypad mapping. Return the answer in any order.

Example:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Input: digits = ""
    Output: []
"""
from typing import List

DIGIT_TO_LETTERS = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    result = []

    def dfs(i, path):
        if i == len(digits):
            result.append(path)
            return
        for ch in DIGIT_TO_LETTERS[digits[i]]:
            dfs(i + 1, path + ch)

    dfs(0, "")
    return result


def test_letterCombinations():
    assert sorted(letterCombinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )
    assert letterCombinations("") == []


if __name__ == "__main__":
    test_letterCombinations()
    print("OK")
