
# 96. Unique Binary Search Trees

# https://leetcode.com/problems/unique-binary-search-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for root_val in range(1, i + 1):
                left = root_val - 1
                right = i - root_val
                dp[i] += dp[left] * dp[right]
        return dp[n]
