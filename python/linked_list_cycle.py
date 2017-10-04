
# 141. Linked List Cycle

# https://leetcode.com/problems/linked-list-cycle/description/
# https://discuss.leetcode.com/topic/618/by-saying-using-no-extra-space-does-it-mean-o-0-in-space/2
# fast runner move 2 steps at one time, slow runner move 1 step
# if traverse to null, there must be no loop


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


    # # space complexity: O(n)
    # visited = list()
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if head is None:
    #         return False
    #     if head in self.visited:
    #         return True
    #     self.visited.append(head)
    #     return self.hasCycle(head.next)
