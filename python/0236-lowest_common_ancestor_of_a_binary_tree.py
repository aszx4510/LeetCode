
# 236. Lowest Common Ancestor of a Binary Tree

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # A concise version, reference to #235
        if root is p or root is q or root is None:
            return root

        lca_left = self.lowestCommonAncestor(root.left, p, q)
        lca_right = self.lowestCommonAncestor(root.right, p, q)

        return root if lca_left and lca_right else lca_left or lca_right


        # My method
        if not root:
            return None
        if root.val == p.val:
            return p
        elif root.val == q.val:
            return q

        lca_left = self.lowestCommonAncestor(root.left, p, q)
        lca_right = self.lowestCommonAncestor(root.right, p, q)

        if lca_left and lca_right:
            return root
        elif lca_left:
            return lca_left
        elif lca_right:
            return lca_right
        return None
