
# 23. Merge k Sorted Lists

# https://leetcode.com/problems/merge-k-sorted-lists/
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue/281748
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue/387296


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = head = ListNode(0)

        # It handles the case of a "tie" when two list nodes have the same value. When that happens, Python will look at the next value in the tuple (in this case, idx), and sort based on that value. Without `idx`, a "tie" would error out if the next value in the tuple were a ListNode (which can't be compared).
        queue = [(head.val, idx, head) for idx, head in enumerate(lists) if head is not None]
        heapq.heapify(queue)

        while queue:
            val, idx, node = heapq.heappop(queue)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(queue, (node.next.val, idx, node.next))
        return head.next
