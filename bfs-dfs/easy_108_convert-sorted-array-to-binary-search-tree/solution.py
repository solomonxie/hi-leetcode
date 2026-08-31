# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    mid = len(nums) // 2  # pick the middle element as root to keep the tree balanced
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


def to_list(root):
    if not root:
        return None
    return [root.val, to_list(root.left), to_list(root.right)]


if __name__ == "__main__":
    print(to_list(sortedArrayToBST([-10, -3, 0, 5, 9])))
