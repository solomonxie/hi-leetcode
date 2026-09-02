"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, return all combinations of well-formed
parentheses.

Example:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
from typing import List


def generate_parenthesis(n: int) -> List[str]:
    result = []
    path = []

    def backtrack(open_count, close_count):
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        if open_count < n:
            path.append("(")
            backtrack(open_count + 1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count + 1)
            path.pop()

    backtrack(0, 0)
    return result


def test_generate_parenthesis():
    assert sorted(generate_parenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )


if __name__ == "__main__":
    test_generate_parenthesis()
    print("OK")
