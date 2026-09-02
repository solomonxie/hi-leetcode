"""
337. House Robber III
https://leetcode.com/problems/house-robber-iii/

The houses form a binary tree; direct-connected houses cannot both be
robbed on the same night. Given the root, return the maximum amount of
money that can be robbed without alerting the police.

Example:
    Input: root = [3,2,3,null,3,null,1]
    Output: 7

    Input: root = [3,4,5,1,3,null,1]
    Output: 9
"""
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: Optional[TreeNode]) -> int:
    def dfs(node) -> Tuple[int, int]:
        # return value packs two facts: (best if robbed, best if not robbed).
        if node is None:
            return 0, 0
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)
        robbed = node.val + left_skip + right_skip
        skipped = max(left_rob, left_skip) + max(right_rob, right_skip)
        return robbed, skipped

    return max(dfs(root))


def test_rob():
    tree = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    assert rob(tree) == 7

    tree2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    assert rob(tree2) == 9


if __name__ == "__main__":
    test_rob()
    print("OK")
