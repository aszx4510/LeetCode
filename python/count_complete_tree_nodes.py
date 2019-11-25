
# 222. Count Complete Tree Nodes

# https://leetcode.com/problems/count-complete-tree-nodes/
# https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # Runtime: 76 ms, faster than 95.70% of Python3
        # Memory Usage: 19.9 MB, less than 100.00% of Python3
        def get_depth(node):
            if not node:
                return 0
            return get_depth(node.left) + 1

        if not root:
            return 0
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)


        # My method with lower efficiency
        # 18 / 18 test cases passed. Runtime: 88 ms, Memory Usage: 20 MB
        def dfs(node):
            if not node:
                return
            else:
                ans[0] += 1
            dfs(node.left)
            dfs(node.right)
            return
        ans = [0]
        dfs(root)
        return ans[0]
