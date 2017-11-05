
# 543. Diameter of Binary Tree

# https://leetcode.com/problems/diameter-of-binary-tree/description/
# https://discuss.leetcode.com/topic/83481/python-simple-with-explanation


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 1

        def depth(root):
            if root is None:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            self.best = max(self.best, left_depth + right_depth + 1)
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.best - 1
        