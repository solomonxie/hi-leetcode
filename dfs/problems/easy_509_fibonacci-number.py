"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers form a sequence such that each number is the sum
of the two preceding ones, starting from 0 and 1. Given n, calculate
F(n).

Example:
    Input: n = 4
    Output: 3

    Input: n = 2
    Output: 1
"""


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def test_fib():
    assert fib(2) == 1
    assert fib(4) == 3
    assert fib(10) == 55


if __name__ == "__main__":
    test_fib()
    print("OK")
