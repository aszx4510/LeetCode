
# 19. Remove Nth Node From End of List

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Approach 2: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for i in range(n + 1):
            if not fast:
                return head.next
            fast = fast.next
        
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        
        return head
