
# 1305. All Elements in Two Binary Search Trees

# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/464368/Short-O(n)-Python


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root1)
        dfs(root2)

        # We can sort two pre-sorted list in O(n) with Timsort
        return sorted(values)
