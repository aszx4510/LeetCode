
# 124. Binary Tree Maximum Path Sum

# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39919/8-10-lines-two-solutions/334879


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            left_val = dfs(node.left) if node.left else 0
            right_val = dfs(node.right) if node.right else 0
            node_max = node.val + max(0, left_val, right_val)
            self.result = max(self.result, node_max, node.val + left_val + right_val)
            return node_max

            # My logic is too complicate
            # self.result = max(self.result, node.val, node.val + left_val, node.val + right_val, 
            #     node.val + left_val + right_val)
            # return max(node.val, node.val + left_val, node.val + right_val)
        self.result = float('-inf')
        dfs(root)
        return self.result
