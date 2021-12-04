
# 147. Insertion Sort List

# https://leetcode.com/problems/insertion-sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # My method is also correct
        if not head or not head.next:
            return head
        start = head
        curr_prev, current = head, head.next
        while current:
            if not curr_prev or current.val < curr_prev.val:
                insert_point = start
                insert_prev = None
                while current.val > insert_point.val:
                    insert_prev = insert_point
                    insert_point = insert_point.next
                curr_prev.next = current.next
                if not insert_prev:  # First node
                    start = current
                else:
                    insert_prev.next = current
                current.next = insert_point
                current = curr_prev

            curr_prev = current
            current = current.next
        return start
