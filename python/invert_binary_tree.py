
# 226. Invert Binary Tree

# https://leetcode.com/problems/invert-binary-tree/description/
# https://discuss.leetcode.com/topic/16039/straightforward-dfs-recursive-iterative-bfs-solutions
# https://discuss.leetcode.com/topic/16062/3-4-lines-python


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


        # my method is more similar with making own stack
        if root is None:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
