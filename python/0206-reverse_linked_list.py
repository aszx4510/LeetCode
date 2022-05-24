
# 206. Reverse Linked List

# https://leetcode.com/problems/reverse-linked-list/description/
# https://discuss.leetcode.com/topic/14043/python-iterative-and-recursive-solution
# https://leetcode.com/problems/reverse-linked-list/solution/


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative
        prev = None
        while head is not None:
            next_node = head.next  # Record the head of next round
            head.next = prev
            prev = head
            head = next_node  # Move to next node
        return prev


        # Recursively
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
