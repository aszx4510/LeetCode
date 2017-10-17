
# 257. Binary Tree Paths

# https://leetcode.com/problems/binary-tree-paths/description/
# https://discuss.leetcode.com/topic/21559/python-solutions-dfs-stack-bfs-queue-dfs-recursively
# a very good solution include various methods


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        return self.get_path(root, '')

        
    def get_path(self, root, path):
        if root.left is None and root.right is None:  # leaf
            path += str(root.val)
            return [path]
        else:
            path += str(root.val) + '->'

        path_list = list()
        if root.left is not None:
            path_list.extend(self.get_path(root.left, path))
        if root.right is not None:
            path_list.extend(self.get_path(root.right, path))
        return path_list
