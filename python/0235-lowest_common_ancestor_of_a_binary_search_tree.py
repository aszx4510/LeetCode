
# 235. Lowest Common Ancestor of a Binary Search Tree

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# https://discuss.leetcode.com/topic/18387/3-lines-with-o-1-space-1-liners-alternatives


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # for Binary Search Tree (BST)
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]  # [p.val > root.val] will be the [0] or [1]
        return root


        # my method for any binary tree
        # if root is p or root is q or root is None:
        #     return root

        # left_lca = self.lowestCommonAncestor(root.left, p, q)
        # right_lca = self.lowestCommonAncestor(root.right, p, q)
        # return root if left_lca and right_lca else left_lca or right_lca
