
# 637. Average of Levels in Binary Tree

# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Breadth-first Search (BFS)
        # copy from the other submissions
        level = [root]
        res = list()
        while level:
            count = len(level)
            res.append(sum(l.val for l in level) * 1.0 / count)
            level = [child for item in level for child in (item.left, item.right) if child]
        return res


        # Depth-first Search (DFS)
        self.record = dict()
        def dfs(root, level):
            if root is None:
                return
            self.record.setdefault(level, []).append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            return
        dfs(root, 0)
        return [sum(values) / float(len(values)) for _, values in self.record.items()]
