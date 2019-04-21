
# 98. Validate Binary Search Tree

# https://leetcode.com/problems/validate-binary-search-tree/


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_BST(root, start, end):
            if not root:
                return True
            if not start < root.val < end:
                return False
            return check_BST(root.left, start, root.val) and check_BST(root.right, root.val, end)
        return check_BST(root, -9999999999999, 9999999999999)
