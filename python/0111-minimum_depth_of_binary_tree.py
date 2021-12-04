
# 111. Minimum Depth of Binary Tree

# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# https://discuss.leetcode.com/topic/16869/3-lines-in-every-language
# We need to add the smaller one of the child depths - except if that's zero, then add the larger one.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        letf_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return (min(letf_depth, right_depth) or max(letf_depth, right_depth)) + 1
