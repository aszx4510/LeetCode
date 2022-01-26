
# 1305. All Elements in Two Binary Search Trees

# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/solution/
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/464368/Short-O(n)-Python


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # One-pass linear
        stack1, stack2, ans = [], [], []
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # Add the smallest value into answer list
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                ans.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                ans.append(root2.val)
                root2 = root2.right
        return ans


        # My version that refers to the discussion post
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
