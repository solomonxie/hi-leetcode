"""
Run: python3 hello_dfs_06_multiple_choices.py

Recap: step 5 recursed into exactly two fixed children, left and right.

Step 6: multiple recursive choices — a call can loop over any number of
options and recurse once per option, instead of calling itself a fixed
number of times. The "state" passed down (the partial answer built so
far) is still immutable here — each recursive call gets its own new copy
(`path + ch`) — so there's no undo to manage yet; that comes later.

The mental model: "at this call, what are ALL the options right now?"
then recurse once per option, each with its own extended copy of the
state — a for-loop of recursive calls instead of a fixed left/right pair.

Speedrun:
  - dfs/problems/medium_17_letter-combinations-of-a-phone-number.py
      Same shape as below, run directly on LeetCode's exact signature.
"""
from typing import List

DIGIT_TO_LETTERS = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    result = []

    def dfs(i, path):
        if i == len(digits):
            result.append(path)
            return
        for ch in DIGIT_TO_LETTERS[digits[i]]:   # every option at this call
            dfs(i + 1, path + ch)                # each gets its own extended copy

    dfs(0, "")
    return result


def test_letter_combinations():
    assert sorted(letter_combinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )
    assert letter_combinations("") == []


if __name__ == "__main__":
    test_letter_combinations()
    print("OK")
