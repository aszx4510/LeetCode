
# 109. Convert Sorted List to Binary Search Tree

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Approach 1: Recursion
        if not head:
            return None

        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        if prev:  # Split the ListNode
            prev.next = None

        root = TreeNode(slow.val)
        if slow == head:  # Only one element
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


        # Approach 2: Array and Recursion
        def list2bst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(array[mid])
            if left == right:
                return root
            root.left = list2bst(left, mid - 1)
            root.right = list2bst(mid + 1, right)
            return root
        
        array = []  # Convert to array
        while head:
            array.append(head.val)
            head = head.next
        return list2bst(0, len(array) - 1)


        # Apporach 3: Inorder Simulation
        def convert(left, right):
            nonlocal head
            if left > right:
                return None
            mid = (left + right) // 2
            # Simulate inorder traversal, recursively enter the left half
            left_node = convert(left, mid - 1)
            root = TreeNode(head.val)
            root.left = left_node

            head = head.next
            root.right = convert(mid + 1, right)
            return root

        n, start = 0, head  # Count the size of ListNode
        while start:
            n += 1
            start = start.next
        return convert(0, n - 1)
