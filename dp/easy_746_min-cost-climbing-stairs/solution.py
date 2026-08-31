# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    prev, curr = 0, 0  # min cost to reach step 0, step 1
    for i in range(2, n + 1):
        prev, curr = curr, min(curr + cost[i - 1], prev + cost[i - 2])
    return curr


if __name__ == "__main__":
    print(minCostClimbingStairs([10, 15, 20]))  # 15
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
