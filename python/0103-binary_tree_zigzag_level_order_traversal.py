
# 103. Binary Tree Zigzag Level Order Traversal

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # Breadth Fisrt Search by using queue
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            temp = []
            node_num = len(queue)
            for i in range(node_num):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp)
        for i in range(1, len(result), 2):
            result[i].reverse()
        return result


        # Another method for Breadth Fisrt Search by using queue
        if not root:
            return []
        queue = [root]
        result, order = [], True
        while queue:
            temp = []
            node_num = len(queue)
            for i in range(node_num):
                node = queue.pop(0)
                if order:
                    temp.append(node.val)
                else:
                    temp.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp)
            order = not order
        return result
