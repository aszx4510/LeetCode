
# 572. Subtree of Another Tree

# https://leetcode.com/problems/subtree-of-another-tree/description/
# https://discuss.leetcode.com/topic/88700/easy-o-n-java-solution-using-preorder-traversal


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # preorder traversal (DFS)
        self.temp = ''

        def generate_preorder_string(node):
            if node is None:
                self.temp += ',#'
                return
            self.temp += ',' + str(node.val)
            generate_preorder_string(node.left)
            generate_preorder_string(node.right)
            return

        generate_preorder_string(s)
        full_tree = self.temp
        self.temp = ''  # reset temp
        generate_preorder_string(t)
        subtree = self.temp
        return True if subtree in full_tree else False


        # my method
        def is_same(s, t):
            if s is None or t is None:
                if s == t:
                    return True
                else:
                    return False
            if s.val != t.val:
                return False
            return is_same(s.left, t.left) and is_same(s.right, t.right)

        if s is None or t is None:
            return False
        return is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
