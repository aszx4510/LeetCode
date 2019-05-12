
# 113. Path Sum II

# https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, target, sum, path):
            if not root:
                return

            path.append(root.val)
            temp_sum = sum + root.val
            if temp_sum == target and not (root.left or root.right):
                result.append(path[:])
            dfs(root.left, target, temp_sum, path)
            dfs(root.right, target, temp_sum, path)
            path.pop()
            return

        result = []
        dfs(root, sum, 0, [])
        return result
