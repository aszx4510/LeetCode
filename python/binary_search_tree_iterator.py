
# 173. Binary Search Tree Iterator

# https://leetcode.com/problems/binary-search-tree-iterator/
# https://leetcode.com/problems/binary-search-tree-iterator/discuss/52525/My-solutions-in-3-languages-with-Stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAllLeftNode(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack:
            node = self.stack.pop()
            self.pushAllLeftNode(node.right)
            return node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.stack else False
        
    def pushAllLeftNode(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
