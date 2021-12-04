
# 138. Copy List with Random Pointer

# https://leetcode.com/problems/copy-list-with-random-pointer/
# https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43488/Java-O(n)-solution


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        mapping = {None: None}

        # First loop: copy all the nodes
        node = head
        while node:
            mapping[node] = Node(node.val, None, None)
            node = node.next

        # Second loop: assign next and random pointers
        node = head
        while node:
            mapping[node].next = mapping[node.next]
            mapping[node].random = mapping[node.random]
            node = node.next

        return mapping[head]

        # # My method
        # mapping = {}
        # if head:
        #     start = Node(head.val, None, None)
        #     mapping[head.val] = start
        # else:
        #     return None

        # while head:
        #     current, random_next, head = head, head.random, head.next

        #     if random_next:
        #         if random_next.val in mapping.keys():
        #             random_node = mapping[random_next.val]
        #         else:
        #             random_node = Node(random_next.val, None, None)
        #             mapping[random_next.val] = random_node
        #     else:
        #         random_node = None

        #     if head:
        #         if head.val in mapping.keys():
        #             next_node = mapping[head.val]
        #         else:
        #             next_node = Node(head.val, None, None)
        #             mapping[head.val] = next_node
        #     else:
        #         next_node = None

        #     if current.val in mapping.keys():
        #         current_node = mapping[current.val]
        #         current_node.next = next_node
        #         current_node.random = random_node
        #     else:
        #         current_node = Node(current.val, next_node, random_node)
        #         mapping[current.val] = current_node
        # return start
