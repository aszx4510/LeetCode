
# 708. Insert into a Sorted Circular Linked List

# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/discuss/1605599/Clean-python-solution-in-O(n)
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/solution/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(val=insertVal)
        
        if not head:
            node.next = node
            return node
    
        prev, curr = head, head.next
        while prev.next != head:
            # Case 1: 1 -> Node(2) -> 3
            if prev.val <= node.val <= curr.val:
                break
            
            # Case 2: 1 -> 3 -> Node(5) -> 1
            #      or 1 -> 3 -> Node(0) -> 5
            if (prev.val > curr.val) and (node.val > prev.val or node.val < curr.val):
                break
            prev, curr = prev.next, curr.next
                
        prev.next = node
        node.next = curr
        return head
