"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase with n steps. Each time you can climb 1 or
2 steps. In how many distinct ways can you climb to the top?

Example:
    Input: n = 2
    Output: 2

    Input: n = 3
    Output: 3
"""


def climb_stairs(n: int) -> int:
    def dfs(k):
        if k <= 2:
            return k
        return dfs(k - 1) + dfs(k - 2)

    return dfs(n)


def test_climb_stairs():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8


if __name__ == "__main__":
    test_climb_stairs()
    print("OK")
