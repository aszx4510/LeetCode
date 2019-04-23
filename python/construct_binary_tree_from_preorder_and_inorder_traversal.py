
# 105. Construct Binary Tree from Preorder and Inorder Traversal

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution./174743


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Readable version with higher efficiency
        def dfs_helper(left, right):
            if not preorder:
                return
            root_val = preorder.pop(0)
            root_index = inorder_map[root_val]
            root = TreeNode(root_val)
            if root_index != left:
                root.left = dfs_helper(left, root_index - 1)
            if root_index != right:
                root.right = dfs_helper(root_index + 1, right)
            return root

        inorder_map = {v: i for i, v in enumerate(inorder)}
        return dfs_helper(0, len(inorder) - 1)


        # Magic
        if inorder:
            root_index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_index])
            root.left = self.buildTree(preorder, inorder[:root_index])
            root.right = self.buildTree(preorder, inorder[root_index + 1:])
            return root
