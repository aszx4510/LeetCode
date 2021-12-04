
# 102. Binary Tree Level Order Traversal

# https://leetcode.com/problems/binary-tree-level-order-traversal/
# https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33450/Java-solution-with-a-queue-used


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return result


        # Depth First Search
        def dfs(root, height):
            if not root:
                return
            if height > len(result):
                result.append([])
            dfs(root.left, height + 1)
            dfs(root.right, height + 1)
            result[height - 1].append(root.val)

        result = []
        dfs(root, 1)
        return result
