
# 687. Longest Univalue Path

# https://leetcode.com/problems/longest-univalue-path/description/
# https://discuss.leetcode.com/topic/105619/python-simple-to-understand


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_path = [0]

        def dfs(node):
            if node is None:
                return 0
            left_len, right_len = dfs(node.left), dfs(node.right)
            left = (left_len + 1) if node.left is not None and node.left.val == node.val else 0
            right = (right_len + 1) if node.right is not None and node.right.val == node.val else 0
            max_path[0] = max(max_path[0], left + right)
            return max(left, right)
        dfs(root)
        return max_path[0]
