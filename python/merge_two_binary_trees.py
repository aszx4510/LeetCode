
# 617. Merge Two Binary Trees

# https://leetcode.com/problems/merge-two-binary-trees/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # first check for root
        if t1 is None:
            return t2
        elif t2 is None:
            return t1

        t1.val += t2.val
        if t1.left is None and t2.left is not None:
            t1.left = t2.left
        else:
            self.mergeTrees(t1.left, t2.left)
        if t1.right is None and t2.right is not None:
            t1.right = t2.right
        else:
            self.mergeTrees(t1.right, t2.right)
        return t1
