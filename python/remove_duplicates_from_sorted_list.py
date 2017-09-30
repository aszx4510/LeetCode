
# 83. Remove Duplicates from Sorted List

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# https://discuss.leetcode.com/topic/31619/simple-iterative-python-6-lines-60-ms


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

        # My answer, very redundant and wordy
        # if not head or not head.next:
        #     return head
        # current = head
        # temp = head.next
        # while True:
        #     if not temp.next:
        #         break
        #     if current.val == temp.val:
        #         temp = temp.next
        #     else:
        #         current.next = temp
        #         current = current.next
        #         temp = temp.next
        # if current.val == temp.val:
        #     current.next = None
        # else:
        #     current.next = temp
        #     print(current.next)
        # return head
