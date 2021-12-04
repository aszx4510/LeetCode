
# 114. Flatten Binary Tree to Linked List

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Post order traversal
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        return
    prev = None


        # My method
        if not root or not(root.left or root.right):
            return
        left = root.left
        right = root.right
        self.flatten(root.left)
        self.flatten(root.right)
        if left:
            right_leaf = left
            while right_leaf.right:
                right_leaf = right_leaf.right
            root.left = None
            root.right = left
            right_leaf.right = right
        return
