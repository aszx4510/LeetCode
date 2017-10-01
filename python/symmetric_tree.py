
# 101. Symmetric Tree

# https://leetcode.com/problems/symmetric-tree/description/
# BFS is another good method


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if not p and not q:
            return True
        if (not p) or (not q):  # (None, None) won't go here
            return False
        return (p.val == q.val) and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
