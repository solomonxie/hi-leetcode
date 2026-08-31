"""
556. Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/

Given a positive integer n, find the smallest integer which has exactly
the same digits as n and is strictly greater than n. If no such positive
integer exists, return -1. The answer must fit in a 32-bit integer.

Example:
    Input: n = 12
    Output: 21

    Input: n = 21
    Output: -1
"""


def nextGreaterElement(n: int) -> int:
    digits = list(str(n))
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i < 0:
        return -1
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    result = int("".join(digits))
    return result if result <= 2**31 - 1 else -1


def test_nextGreaterElement():
    assert nextGreaterElement(12) == 21
    assert nextGreaterElement(21) == -1


if __name__ == "__main__":
    test_nextGreaterElement()
    print("OK")
