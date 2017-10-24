
# 404. Sum of Left Leaves

# https://leetcode.com/problems/sum-of-left-leaves/description/
# https://discuss.leetcode.com/topic/60395/4-lines-python-recursive-ac-solution


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # check left leaf
        if root.left is not None and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


    # my method
    # def sumOfLeftLeaves(self, root):
    #     return self.sum_of_left_leaves(root, False)


    # def sum_of_left_leaves(self, root, is_left):
    #     if root is None:
    #         return 0
    #     if root.left is None and root.right is None:  # leaves
    #         if is_left:
    #             return root.val
    #         else:
    #             return 0
    #     return self.sum_of_left_leaves(root.left, True) + self.sum_of_left_leaves(root.right, False)
