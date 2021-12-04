
# 206. Reverse Linked List

# https://leetcode.com/problems/reverse-linked-list/description/
# https://discuss.leetcode.com/topic/14043/python-iterative-and-recursive-solution


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iterative
        prev = None
        while head is not None:
            next_node = head.next  # record the head of next round
            head.next = prev
            prev = head
            head = next_node  # move to next node
        return prev

        # recursively
        return self.reverse(head)


    def reverse(self, node, prev=None):
        if node is None:
            return prev
        next_node = node.next
        node.next = prev
        return self.reverse(next_node, node)
