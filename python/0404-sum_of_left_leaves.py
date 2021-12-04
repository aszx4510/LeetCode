
# 404. Sum of Left Leaves

# https://leetcode.com/problems/sum-of-left-leaves/description/
# https://discuss.leetcode.com/topic/60395/4-lines-python-recursive-ac-solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # check left leaf
        if root.left is not None and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


    # my method
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            elif not node.left and not node.right and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)
