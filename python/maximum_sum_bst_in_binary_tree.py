
# 1373. Maximum Sum BST in Binary Tree

# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, True
            left_sum, left_bst = dfs(root.left)
            right_sum, right_bst = dfs(root.right)
            larger_than_left = root.left.val < root.val if root.left else True
            smaller_than_right = root.val < root.right.val if root.right else True
            if left_bst and right_bst and larger_than_left and smaller_than_right:
                temp = left_sum + right_sum + root.val
                result[0] = max(result[0], temp)
                return temp, True
            return 0, False

        result = [0]
        dfs(root)
        return result[0]
