
# 1290. Convert Binary Number in a Linked List to Integer

# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
