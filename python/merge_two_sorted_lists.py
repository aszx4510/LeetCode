
# 21. Merge Two Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/description/
# https://discuss.leetcode.com/topic/21292/python-solutions-iteratively-recursively-iteratively-in-place


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        zero = current = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            # go to next node
            current = current.next
        current.next = l1 or l2
        return zero.next
