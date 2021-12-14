
# 938. Range Sum of BST

# https://leetcode.com/problems/range-sum-of-bst/
# https://leetcode.com/problems/range-sum-of-bst/solution/
# https://leetcode.com/problems/range-sum-of-bst/discuss/192019/JavaPython-3-3-similar-recursive-and-1-iterative-methods-w-comment-and-analysis.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # DFS
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans


        # Concise version
        if not root:
            return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


        # My version
        def tree_sum(root):
            if not root:
                return 0
            return root.val + tree_sum(root.left) + tree_sum(root.right)

        def tree_sum_below_target(root, target):
            if not root:
                return 0

            if root.val == target:
                return target + tree_sum(root.left)
            elif root.val < target:
                return root.val + tree_sum(root.left) + tree_sum_below_target(root.right, target)
            else:
                return tree_sum_below_target(root.left, target)

        return tree_sum_below_target(root, high) - tree_sum_below_target(root, low) + low
