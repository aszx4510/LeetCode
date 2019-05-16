
# 117. Populating Next Right Pointers in Each Node II

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


# Definition for a Node.
# class Node:
#     def __init__(self, val, left, right, next):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        # Breadth-First Search
        level = 0
        queue = [root]
        while queue:
            prev = None
            for _ in range(pow(2, level)):
                node = queue.pop(0)
                if prev:
                    prev.next = node
                prev = node
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
            level += 1
        return root
