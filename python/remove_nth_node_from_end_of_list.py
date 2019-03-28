
# 19. Remove Nth Node From End of List

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Approach 2: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start, herald = head, head
        for i in range(n + 1):
            if not herald:
                return head.next
            herald = herald.next
        while herald:
            start = start.next
            herald = herald.next
        start.next = start.next.next
        return head
