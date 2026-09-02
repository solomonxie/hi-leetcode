"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top. Each time
you can either climb 1 or 2 steps. In how many distinct ways can you climb
to the top?

Example:
    Input: n = 2
    Output: 2
    Explanation: 1+1 step, or 2 steps.

    Input: n = 3
    Output: 3
    Explanation: 1+1+1, 1+2, or 2+1.
"""


def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def test_climbStairs():
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3


if __name__ == "__main__":
    test_climbStairs()
    print("OK")
