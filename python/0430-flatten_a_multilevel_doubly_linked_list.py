
# 430. Flatten a Multilevel Doubly Linked List

# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/154908/Python-easy-solution-using-stack/350757


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # Stack
        if not head:
            return head

        stack = [head]
        prev = Node(0, None, None, None)
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            prev = root
            
            # Push first but pop last
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
                root.child = None
        
        head.prev = None
        return head


        # My method by using recursion
        def dfs(parent, node):
            if not node:
                return node

            node.prev = parent

            while node.next and not node.child:
                node = node.next

            if node.child:
                node_next = node.next
                last = dfs(node, node.child)
                node.next = node.child
                node.child = None

                if node_next:
                    last.next = node_next
                    node_next.prev = last

            while node.next and not node.child:
                node = node.next

            return node
        dfs(None, head)
        return head
