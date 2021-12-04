
# 92. Reverse Linked List II

# https://leetcode.com/problems/reverse-linked-list-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        fake_head = ListNode(0)
        fake_head.next = head
        head = fake_head
        for i in range(m - 1):
            head = head.next
        
        # Get pre-node of starting point
        pre_reverse = head
        head = head.next

        # Start reverse
        reverse_start_point = head
        pre = None
        for i in range(n - m + 1):
            next_node = head
            head = next_node.next
            if next_node and pre:
                next_node.next = pre
            pre = next_node
        pre_reverse.next = next_node
        reverse_start_point.next = head

        return fake_head.next
