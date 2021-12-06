
# 337. House Robber III

# https://leetcode.com/problems/house-robber-iii/
# https://leetcode.com/problems/house-robber-iii/solution/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Dynamic Programming
        if not root:
            return 0

        # Reform tree into array-based tree
        tree = []
        graph = {-1: []}
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))

        robbed, not_robbed = [0] * (index + 1), [0] * (index + 1)
        for i in reversed(range(index + 1)):  # Bottom-up
            if not graph[i]:  # Leaf
                robbed[i] = tree[i]
                not_robbed[i] = 0
            else:
                robbed[i] = tree[i] + sum(not_robbed[child] for child in graph[i])
                not_robbed[i] = sum(max(robbed[child], not_robbed[child]) for child in graph[i])

        return max(robbed[0], not_robbed[0])


        # Recursion with memoization
        robbed, not_robbed = {}, {}

        def helper(node, parent_robbed: bool):
            if not node:
                return 0

            if parent_robbed:
                if node in robbed:
                    return robbed[node]
                result = helper(node.left, False) + helper(node.right, False)
                robbed[node] = result
                return result
            else:
                if node in not_robbed:
                    return not_robbed[node]

                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_robbed[node] = result
                return result

        return helper(root, False)
