
# 1022. Sum of Root To Leaf Binary Numbers

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/270025/JavaC%2B%2BPython-Recursive-Solution


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, num):
            if not node:
                return 0

            num = num * 2 + node.val
            if node.left == node.right:  # Leaf
                return num
            return dfs(node.left, num) + dfs(node.right, num)
        return dfs(root, 0)


        # My version
        def dfs(node, num):
            new_num = num * 2 + node.val

            if not node.left and not node.right:
                return new_num
            left_sum = dfs(node.left, new_num) if node.left else 0
            right_sum = dfs(node.right, new_num) if node.right else 0
            return left_sum + right_sum

        return dfs(root, 0)
