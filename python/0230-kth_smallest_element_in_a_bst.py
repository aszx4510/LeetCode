
# 230. Kth Smallest Element in a BST

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # My version
        def dfs(node, current):
            if not node:
                return current
            left_result = dfs(node.left, current)
            if left_result is None or current > k:
                return None
            current = left_result + 1

            if current == k:
                ans[0] = node.val
                return None
            else:
                return dfs(node.right, current)

        ans = [0]
        dfs(root, 0)
        return ans[0]
