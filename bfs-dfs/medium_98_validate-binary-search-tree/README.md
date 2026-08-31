# 98. Validate Binary Search Tree

LeetCode: https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as: every node's left subtree contains only values strictly less than the node's value, every node's right subtree contains only values strictly greater, and both subtrees must also be BSTs.

## Example

```
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root's value is 5 but its right child's left child is 3, which is less than 5.
```
