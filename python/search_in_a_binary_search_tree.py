
# 700. Search in a Binary Search Tree

# https://leetcode.com/problems/search-in-a-binary-search-tree/
# https://leetcode.com/problems/search-in-a-binary-search-tree/discuss/148890/Python-3-lines-DFS-solution-w-a-very-simple-approach


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Concise version and utilize the original function
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and root.val < val:
            return self.searchBST(root.right, val)
        return root


        # My version
        def binary_search(node):
            if not node:
                return None
            
            if node.val == val:
                return node
            elif node.val < val:
                result = binary_search(node.right)
            else:
                result = binary_search(node.left)
            return result

        return binary_search(root)
