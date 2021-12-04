
# 501. Find Mode in Binary Search Tree

# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
# https://discuss.leetcode.com/topic/77330/java-4ms-beats-100-extra-o-1-solution-no-map


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.prev = None
        self.count, self.max_count = 1, 1
        self.mode_list = list()
        
        self.find_mode(root, self.mode_list)
        return self.mode_list


    def find_mode(self, root, mode_list):
        if root is None:
            return
        self.find_mode(root.left, mode_list)
        if self.prev is not None:
            if self.prev == root.val:
                self.count += 1
            else:
                self.count = 1
        if self.count > self.max_count:
            self.max_count = self.count
            self.mode_list = []  # self.mode_list.clear()
            self.mode_list.append(root.val)
        elif self.count == self.max_count:
            self.mode_list.append(root.val)
        self.prev = root.val
        self.find_mode(root.right, mode_list)
        return
