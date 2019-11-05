
# 143. Reorder List

# https://leetcode.com/problems/reorder-list/
# https://leetcode.com/problems/reorder-list/discuss/45003/A-concise-O(n)-time-O(1)-in-place-solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Time Complexity:  O(n)
        # Space Complexity: O(1), without using extra space


        if not head:
            return head

        slow, fast = head, head
        prev = slow  # Default value
        while fast and fast.next:  # Split to half
            prev = slow
            slow = slow.next
            fast = fast.next.next
            if fast and not fast.next:  # For odd numbers
                prev = slow
                slow = slow.next
        prev.next = None

        # Reverse second half
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        # Merge two linked list
        start = head
        slow = prev
        while head and slow:
            head_next = head.next
            slow_next = slow.next
            head.next = slow
            slow.next = head_next
            head = head_next
            slow = slow_next                

        return start
