
# 563. Binary Tree Tilt

# https://leetcode.com/problems/binary-tree-tilt/description/
# https://discuss.leetcode.com/topic/87208/python-simple-with-explanation


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # concise version
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


        # my version
        def sum_and_tilt(root):
            if root is None:
                return 0, [0]  # both sum and tilt are 0
            left_sum, left_tilt = sum_and_tilt(root.left)
            right_sum, right_tilt = sum_and_tilt(root.right)
            left_tilt.extend(right_tilt)
            left_tilt.append(abs(left_sum - right_sum))
            print(left_tilt, right_tilt)
            return left_sum + right_sum + root.val, left_tilt

        _, tilt = sum_and_tilt(root)
        return sum(tilt)
