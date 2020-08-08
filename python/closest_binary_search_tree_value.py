
# 270. Closest Binary Search Tree Value

# https://leetcode.com/problems/closest-binary-search-tree-value/
# https://leetcode.com/problems/closest-binary-search-tree-value/solution/
# https://leetcode.com/problems/closest-binary-search-tree-value/discuss/70327/4-7-lines-recursiveiterative-RubyC%2B%2BJavaPython


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # Time Complexity: O(H)
        closest = root.val
        while root:
            closest = min((closest, root.val), key=lambda x: abs(x - target))
            root = root.left if target < root.val else root.right
        return closest
