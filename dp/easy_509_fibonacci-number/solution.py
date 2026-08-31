# https://leetcode.com/problems/fibonacci-number/


def fib(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print(fib(2))  # 1
    print(fib(4))  # 3
