
# 203. Remove Linked List Elements

# https://leetcode.com/problems/remove-linked-list-elements/description/
# https://discuss.leetcode.com/topic/12580/3-line-recursive-solution


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head is not None and head.val == val:
            head = head.next

        node = head
        while node is not None and node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head


        # recursive method, but it will exceed the limitation of recursion depth
        # if head is None:
        #     return head
        # head.next = self.removeElements(head.next, val)
        # return head.next if head.val == val else head
