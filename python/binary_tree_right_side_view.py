
# 199. Binary Tree Right Side View

# https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(node, depth):
            if not node:
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            result[depth] = node.val
        result = {}
        dfs(root, 0)
        return [result[k] for k in sorted(result.keys())]
