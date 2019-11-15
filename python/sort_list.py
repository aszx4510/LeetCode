
# 148. Sort List

# https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def divide(head):
            prev_slow = None
            slow, fast = head, head
            while fast and fast.next:
                prev_slow = slow
                slow = slow.next
                fast = fast.next.next
            
            if slow == fast:
                return slow
            else:
                prev_slow.next = None
                return merge(divide(head), divide(slow))

        def merge(head1, head2):
            prev_start = prev = ListNode(0)
            while head1 and head2:
                if head1.val <= head2.val:
                    prev.next = head1
                    prev = prev.next
                    head1 = head1.next
                else:
                    prev.next = head2
                    prev = prev.next
                    head2 = head2.next
            if head1:
                prev.next = head1
            elif head2:
                prev.next = head2
            return prev_start.next

        return divide(head)
