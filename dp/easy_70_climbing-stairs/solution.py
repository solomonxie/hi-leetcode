# https://leetcode.com/problems/climbing-stairs/


def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2  # ways to reach step 1, step 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print(climbStairs(2))  # 2
    print(climbStairs(3))  # 3
