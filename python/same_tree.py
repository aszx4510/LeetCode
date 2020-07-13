
# 100. Same Tree

# https://leetcode.com/problems/same-tree/discuss/
# https://discuss.leetcode.com/topic/14561/shortest-simplest-python


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q  # True for both p and q are None


        # if p is None and q is None:
        #     return True
        # elif (not p and q) or (p and not q):
        #     return False

        # if not p.val == q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
