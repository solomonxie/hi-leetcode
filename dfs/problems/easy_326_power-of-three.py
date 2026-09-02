"""
326. Power of Three
https://leetcode.com/problems/power-of-three/

Given an integer n, return true if it is a power of three, and false
otherwise.

Example:
    Input: n = 27
    Output: true

    Input: n = 0
    Output: false
"""


def is_power_of_three(n: int) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return is_power_of_three(n // 3)


def test_is_power_of_three():
    assert is_power_of_three(27) is True
    assert is_power_of_three(0) is False
    assert is_power_of_three(45) is False


if __name__ == "__main__":
    test_is_power_of_three()
    print("OK")
