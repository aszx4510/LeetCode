
# 993. Cousins in Binary Tree

# https://leetcode.com/problems/cousins-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val in (x, y):
            return False
        layer = [(root, 0, 0)]
        depth, parent = 0, 0
        while layer:
            node, p, d = layer.pop(0)
            if node.val in (x, y):
                if not depth:
                    depth = d
                    parent = p
                else:
                    return True if depth == d and parent != p else False

            if node.left:
                layer.append((node.left, node.val, d + 1))
            if node.right:
                layer.append((node.right, node.val, d + 1))
        return False
