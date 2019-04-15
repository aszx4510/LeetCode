
# 86. Partition List

# https://leetcode.com/problems/partition-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        part_1, part_2 = ListNode(-1), ListNode(-1)
        part_1_head, part_2_head = part_1, part_2
        while head:
            if head.val < x:
                part_1.next = head
                part_1 = part_1.next
            else:
                part_2.next = head
                part_2 = part_2.next
            head = head.next
            
        if not part_1_head.next:
            return part_2_head.next
        elif not part_2_head.next:
            return part_1_head.next
        else:
            part_1.next = part_2_head.next
            part_2.next = None
        return part_1_head.next
