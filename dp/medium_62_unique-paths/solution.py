# https://leetcode.com/problems/unique-paths/


def uniquePaths(m: int, n: int) -> int:
    row = [1] * n  # paths to reach each cell in the current row
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


if __name__ == "__main__":
    print(uniquePaths(3, 7))  # 28
    print(uniquePaths(3, 2))  # 3
