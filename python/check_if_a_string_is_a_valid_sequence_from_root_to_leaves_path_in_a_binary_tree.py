
# 30-Day LeetCoding Challenge: Week 5 Day 2
# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/


# Definition for a binary tree node.
#class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            return False

        if len(arr) == 1:
            if root.val == arr[0] and not root.left and not root.right:
                return True
            else:
                return False
        else:
            if root.val == arr[0]:
                return self.isValidSequence(root.left, arr[1:]) or self.isValidSequence(root.right, arr[1:])
            else:
                return False
