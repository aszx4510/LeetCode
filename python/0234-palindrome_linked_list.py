
# 234. Palindrome Linked List

# https://leetcode.com/problems/palindrome-linked-list/description/
# https://discuss.leetcode.com/topic/18293/11-lines-12-with-restore-o-n-time-o-1-space


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        slow = fast = head
        while fast and fast.next is not None:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        if fast is not None:  # number of linkedlist is odd, skip the middle node 
            slow = slow.next
        while reverse and reverse.val == slow.val:
            slow = slow.next
            reverse = reverse.next
        return not reverse
