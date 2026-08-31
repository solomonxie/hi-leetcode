"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers form a sequence where each number is the sum of the
two preceding ones, starting from 0 and 1: F(0) = 0, F(1) = 1,
F(n) = F(n-1) + F(n-2) for n > 1. Given n, return F(n).

Example:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""


def fib(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def test_fib():
    assert fib(2) == 1
    assert fib(4) == 3


if __name__ == "__main__":
    test_fib()
    print("OK")
