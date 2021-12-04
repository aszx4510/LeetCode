
# 61. Rotate List

# https://leetcode.com/problems/rotate-list/


class Solution(object):
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        last_node, n = head, 1
        while last_node.next:
            last_node = last_node.next
            n += 1
        k = k % n
        if k == 0:  # Doesn't need ratation
            return head
        step = n - k - 1
        fast = head
        for i in range(step):  # faster (n - k - 1) steps
            fast = fast.next
        result = fast.next
        fast.next = None
        last_node.next = head
        return result
