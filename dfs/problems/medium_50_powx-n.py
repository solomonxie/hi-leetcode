"""
50. Pow(x, n)
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n.

Example:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Input: x = 2.10000, n = 3
    Output: 9.26100
"""


def my_pow(x: float, n: int) -> float:
    def dfs(base, exp):
        if exp == 0:
            return 1.0
        half = dfs(base, exp // 2)
        if exp % 2 == 0:
            return half * half
        return half * half * base

    if n < 0:
        return 1 / dfs(x, -n)
    return dfs(x, n)


def test_my_pow():
    assert round(my_pow(2.0, 10), 5) == 1024.0
    assert round(my_pow(2.1, 3), 5) == 9.261
    assert round(my_pow(2.0, -2), 5) == 0.25


if __name__ == "__main__":
    test_my_pow()
    print("OK")
