
# 2. Add Two Numbers

# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add_one = 0
        result = ListNode(None)
        prev = result
        while l1 or l2 or add_one:
            if l1:
                l1_value = l1.val
                l1 = l1.next
            else:
                l1_value = 0

            if l2:
                l2_value = l2.val
                l2 = l2.next
            else:
                l2_value = 0

            temp = l1_value + l2_value + add_one
            add_one = temp // 10
            temp_node = ListNode(temp % 10)
            prev.next = temp_node
            prev = temp_node
        return result.next
