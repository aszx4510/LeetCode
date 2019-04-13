
# 82. Remove Duplicates from Sorted List II

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = slow = ListNode(None)
        fast = head
        while fast:
            if fast.next and fast.val == fast.next.val:
                temp = fast.val
                while fast and fast.val == temp:
                    fast = fast.next
                continue

            slow.next = fast
            slow = slow.next
            fast = fast.next
        slow.next = None
        return start.next
