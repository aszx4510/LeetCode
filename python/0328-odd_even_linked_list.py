
# 328. Odd Even Linked List

# https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Concise version
        odds = odds_curr = ListNode(None)
        evens = evens_curr = ListNode(None)
        while head:
            odds_curr.next = head
            evens_curr.next = head.next

            odds_curr = odds_curr.next
            evens_curr = evens_curr.next

            head = head.next.next if evens_curr else None
        
        odds_curr.next = evens.next
        return odds.next


        # My method
        if not head:
            return head
            
        even_head = head.next
        odd_curr, even_curr = head, even_head

        while odd_curr and even_curr:
            odd_curr.next = odd_curr.next.next if odd_curr.next else None
            even_curr.next = even_curr.next.next if even_curr.next else None

            odd_prev, odd_curr = odd_curr, odd_curr.next
            even_curr = even_curr.next

        if odd_curr:
            odd_curr.next = even_head
        else:
            odd_prev.next = even_head

        return head
