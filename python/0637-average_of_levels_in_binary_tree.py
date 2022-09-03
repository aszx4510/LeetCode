
# 637. Average of Levels in Binary Tree

# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
