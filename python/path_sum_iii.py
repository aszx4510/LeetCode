
# 437. Path Sum III

# https://leetcode.com/problems/path-sum-iii/description/
# https://discuss.leetcode.com/topic/65100/python-solution-with-detailed-explanation


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        self.result = 0
        self.helper(root, 0, sum, {0: 1})
        # {0: 1} means the path definitely equal to sum, and the count of path is 1
        return self.result


    def helper(self, root, current_sum, sum, cache):
        if root is not None:
            complement = current_sum + root.val - sum
            if complement in cache:
                self.result += cache[complement]
            cache[current_sum + root.val] = cache.get(current_sum + root.val, 0) + 1
            self.helper(root.left, current_sum + root.val, sum, cache)
            self.helper(root.right, current_sum + root.val, sum, cache)
            cache[current_sum + root.val] -= 1
        return
