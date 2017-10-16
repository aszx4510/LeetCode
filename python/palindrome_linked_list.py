
# 234. Palindrome Linked List

# https://leetcode.com/problems/palindrome-linked-list/description/
# https://discuss.leetcode.com/topic/18293/11-lines-12-with-restore-o-n-time-o-1-space


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # reverse the first half
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
