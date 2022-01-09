
# 1026. Maximum Difference Between Node and Ancestor


# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            left = dfs(node.left, curr_max, curr_min)
            right = dfs(node.right, curr_max, curr_min)
            return max(left, right)

        if not root:
            return 0

        return dfs(root, root.val, root.val)
