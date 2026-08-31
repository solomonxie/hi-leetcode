# 417. Pacific Atlantic Water Flow

LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an `m x n` rectangular island bordering both the Pacific Ocean (touching the top and left edges) and the Atlantic Ocean (touching the bottom and right edges). `heights[r][c]` represents the height of the cell at `(r, c)`. Rain water can flow from a cell to an adjacent cell with height less than or equal to its own, in the 4 cardinal directions. Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

## Example

```
Input: heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```
