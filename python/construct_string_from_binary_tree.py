
# 606. Construct String from Binary Tree

# https://leetcode.com/problems/construct-string-from-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # concise version
        result = ''
        if t is None:
            return result
        result += str(t.val)
        if t.right is not None:
            result += '(' + self.tree2str(t.left) + ')'
            result += '(' + self.tree2str(t.right) + ')'
        elif t.left is not None:
            result += '(' + self.tree2str(t.left) + ')'
        return result


        # my version
        self.construct = ''

        def _tree2str(root):
            if root is None:
                return
            self.construct += '(' + str(root.val)
            if root.left is None and root.right is not None:
                self.construct += '()'
            else:
                _tree2str(root.left)
            _tree2str(root.right)

            self.construct += ')'
            return

        _tree2str(t)
        return self.construct[1:-1]
