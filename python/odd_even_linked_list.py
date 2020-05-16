
# 328. Odd Even Linked List

# https://leetcode.com/problems/odd-even-linked-list/


class Solution(object):
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Concise version
        odds = odds_curr = ListNode(None)
        evens = evens_curr = ListNode(None)
        while head:
            evens_curr.next = head
            odds_curr.next = head.next

            evens_curr = evens_curr.next
            odds_curr = odds_curr.next

            head = head.next.next if odds_curr else None
        evens_curr.next = odds.next
        return evens.next


        # Another version        
        if not head:
            return head
        result = head
        odds = odds_curr = ListNode(None)
        while head and head.next:
            odds_curr.next = head.next
            odds_curr = odds_curr.next

            head.next = head.next.next
            prev = head
            head = head.next
        if not head:
            head = prev
        head.next = odds.next
        odds_curr.next = None
        return result
