
# 589. N-ary Tree Preorder Traversal

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            for child in reversed(node.children):
                stack.append(child)
            result.append(node.val)
        return result
