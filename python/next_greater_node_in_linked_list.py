
# 1019. Next Greater Node In Linked List

# https://leetcode.com/contest/weekly-contest-130/problems/next-greater-node-in-linked-list/
# https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/265508/JavaC%2B%2BPython-Next-Greater-Element


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = []
        stack = []  # [index, value]
        while head:
            while stack and stack[-1][1] < head.val:
                result[stack.pop()[0]] = head.val
            stack.append([len(result), head.val])
            result.append(0)  # Initialize the value
            head = head.next
        return result
