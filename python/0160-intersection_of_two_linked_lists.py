
# 160. Intersection of Two Linked Lists

# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# https://discuss.leetcode.com/topic/28067/java-solution-without-knowing-the-difference-in-len
# Two interations, two pointer "must" meet at the intersection.
# Second interation should change to the other linked list, and the path will be same.
# If the two linked lists have no intersection, a and b will be None (tail node) simultaneously.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None and headB is None:
            return None

        a, b = headA, headB
        while a is not b:
            a = a.next if a is not None else headB
            b = b.next if b is not None else headA
        return a
