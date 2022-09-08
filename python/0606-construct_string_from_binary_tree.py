
# 606. Construct String from Binary Tree

# https://leetcode.com/problems/construct-string-from-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # concise version
        result = ''
        if root is None:
            return result
        result += str(root.val)
        if root.right is not None:
            result += '(' + self.tree2str(root.left) + ')'
            result += '(' + self.tree2str(root.right) + ')'
        elif root.left is not None:
            result += '(' + self.tree2str(root.left) + ')'
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

        _tree2str(root)
        return self.construct[1:-1]
