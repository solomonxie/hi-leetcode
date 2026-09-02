"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of the i-th
step on a staircase. Once you pay the cost, you can either climb one or
two steps. You can start from step index 0 or 1. Return the minimum cost
to reach the top of the floor (one step past the last index).

Example:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: Start at index 1, pay 15, climb two steps to the top.

    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: Start at index 0, pay 1, then hop every other step:
                 0->2->4->6->7->9->top.
"""
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    prev, curr = 0, 0
    for i in range(2, n + 1):
        prev, curr = curr, min(curr + cost[i - 1], prev + cost[i - 2])
    return curr


def test_minCostClimbingStairs():
    assert minCostClimbingStairs([10, 15, 20]) == 15
    assert minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


if __name__ == "__main__":
    test_minCostClimbingStairs()
    print("OK")
