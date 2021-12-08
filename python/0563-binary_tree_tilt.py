
# 563. Binary Tree Tilt

# https://leetcode.com/problems/binary-tree-tilt/description/
# https://discuss.leetcode.com/topic/87208/python-simple-with-explanation


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # Concise version
        self.tilt = 0
        def node_sum(root):
            if root is None:
                return 0
            left_sum = node_sum(root.left)
            right_sum = node_sum(root.right)
            self.tilt += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val
        node_sum(root)
        return self.tilt


        # My version
        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_tilt = dfs(node.left)
            right_sum, right_tilt = dfs(node.right)

            node_sum = left_sum + right_sum + node.val
            node_tilt = abs(left_sum - right_sum) + left_tilt + right_tilt

            return node_sum, node_tilt
        return dfs(root)[1]
