
# 662. Maximum Width of Binary Tree

# https://leetcode.com/problems/maximum-width-of-binary-tree/
# https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106650/Python...


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        width = 0
        level = [(1, root)]

        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [kid 
                     for num, node in level
                     for kid in enumerate((node.left, node.right), start=num * 2)
                     if kid[1]]  # kid is (num, node)
        return width
