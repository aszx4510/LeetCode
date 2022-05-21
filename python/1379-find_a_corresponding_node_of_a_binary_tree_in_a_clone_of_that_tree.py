
# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Concise version
        def dfs(o, c):
            if o:
                if o == target:
                    return c
                return dfs(o.left, c.left) or dfs(o.right, c.right)
        return dfs(original, cloned)
