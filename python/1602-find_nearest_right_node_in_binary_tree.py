
# 1602. Find Nearest Right Node in Binary Tree

# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/solution/
# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/discuss/873100/Two-Simple-BFS-Solutions-Python


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:

        # Concise version, BFS with two queues
        queue, next_queue = [], [root]
        while next_queue:
            queue, next_queue = next_queue, []

            while queue:
                node = queue.pop(0)
                if node == u:
                    return queue.pop(0) if queue else None

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)


        # My version, BFS with two queues
        queue, next_queue = [], [root]

        while next_queue:
            queue, next_queue = next_queue, []
            if u in queue:
                idx = queue.index(u)
                if idx != len(queue) -1:
                    return queue[idx + 1]
                else:
                    return None
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                