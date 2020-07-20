
# 203. Remove Linked List Elements

# https://leetcode.com/problems/remove-linked-list-elements/description/
# https://discuss.leetcode.com/topic/12580/3-line-recursive-solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Pass the nodes with val from the start point
        while head and head.val == val:
            head = head.next

        # Get the first node doesn't with val
        node = head
        while node and node.next:
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
