
# 129. Sum Root to Leaf Numbers

# https://leetcode.com/problems/sum-root-to-leaf-numbers/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, value):
            node_value = value * 10 + node.val
            if not (node.left or node.right):
                return node_value
            left_value = dfs(node.left, node_value) if node.left else 0
            right_value = dfs(node.right, value * 10 + node.val) if node.right else 0
            return left_value + right_value
        if not root:
            return 0
        return dfs(root, 0)
