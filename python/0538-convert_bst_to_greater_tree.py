
# 538. Convert BST to Greater Tree

# https://leetcode.com/problems/convert-bst-to-greater-tree/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert_greater_tree(root, 0)
        return root

    def convert_greater_tree(self, root, right_sum):
        if root is None:
            return right_sum
        right_sum = self.convert_greater_tree(root.right, right_sum) + root.val
        root.val = right_sum
        right_sum = self.convert_greater_tree(root.left, right_sum)
        return right_sum
