
# 106. Construct Binary Tree from Inorder and Postorder Traversal

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not (inorder and postorder):
            return None

        root = TreeNode(postorder.pop())
        inorder_inedx = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorder_inedx + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_inedx], postorder)
        return root
