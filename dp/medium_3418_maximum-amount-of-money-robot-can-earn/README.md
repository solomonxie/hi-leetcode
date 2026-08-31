# 3418. Maximum Amount of Money Robot Can Earn

LeetCode: https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

You are given an `m x n` grid `coins`, where `coins[i][j]` can be negative (a gangster steals that amount from the robot) or positive (that amount is added). The robot starts at `(0, 0)` and moves only right or down to reach `(m-1, n-1)`. On at most 2 cells during the journey, the robot can neutralize the gangster there, so that cell contributes 0 instead of its value. It is guaranteed there exists a path along which the robot's total money never goes negative. Return the maximum amount of money the robot can have when it reaches the final cell.

## Example

```
Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
Output: 8
Explanation: Path (0,0)->(0,1)->(0,2)->(1,2)->(2,2), neutralizing the -1 at (0,2):
             0 + 1 + 0 + 3 + 4 = 8.

Input: coins = [[10,10,10],[10,10,10]]
Output: 40
```
