
# 107. Binary Tree Level Order Traversal II

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        order = list()
        self.dfs(root, 0, order)
        return list(reversed(order))

    def dfs(self, root, level, order):
        if root:
            if len(order) - 1 < level:
                order.append(list())  # order.insert(0, [])
            order[level].append(root.val)  # order[-(level+1)].append(root.val)
            self.dfs(root.left, level + 1, order)
            self.dfs(root.right, level + 1, order)
