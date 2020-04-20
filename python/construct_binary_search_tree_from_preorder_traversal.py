
# 1008. Construct Binary Search Tree from Preorder Traversal

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252722/Python-stack-solution-beats-100-on-runtime-and-memory


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            node = TreeNode(value)
            if value < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and value > stack[-1].val:
                    prev = stack.pop()
                prev.right = node
                stack.append(node)
        return root
