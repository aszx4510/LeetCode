
# 987. Vertical Order Traversal of a Binary Tree

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231140/Add-clarification-for-the-output-order


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        queue = [(root, 0)]
        result = defaultdict(list)

        while queue:
            new_queue = []
            temp_dict = defaultdict(list)

            for node, position in queue:
                if not node:
                    continue
                temp_dict[position].append(node.val)
                new_queue.append((node.left, position - 1))
                new_queue.append((node.right, position + 1))

            queue = new_queue
            for position, val_list in temp_dict.items():
                result[position].extend(sorted(val_list))
        return [result[key] for key in sorted(result.keys())]


        # This problem want the result order sort from small to large, so DFS won't satisfied that
        def dfs(node, position):
            if not node:
                return

            result[position].append(node.val)
            dfs(node.left, position - 1)
            dfs(node.right, position + 1)

        result = defaultdict(list)
        dfs(root, 0)
        return [sorted(result[key]) for key in sorted(result.keys())]
