
# 437. Path Sum III

# https://leetcode.com/problems/path-sum-iii/description/
# https://discuss.leetcode.com/topic/65100/python-solution-with-detailed-explanation


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(node, target, temp_sum, cache):
            if not node:
                return
            temp_sum += node.val
            complement = temp_sum - target
            result[0] += cache.get(complement, 0)
            cache[temp_sum] = cache.get(temp_sum, 0) + 1
            helper(node.left, target, temp_sum, cache)
            helper(node.right, target, temp_sum, cache)
            cache[temp_sum] -= 1

        result = [0]
        helper(root, sum, 0, {0: 1})
        return result[0]
