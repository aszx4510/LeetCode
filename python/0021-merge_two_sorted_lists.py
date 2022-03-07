
# 21. Merge Two Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/description/
# https://discuss.leetcode.com/topic/21292/python-solutions-iteratively-recursively-iteratively-in-place


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        zero = current = ListNode(0)

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # go to next node
            current = current.next
        current.next = list1 or list2
        return zero.next
