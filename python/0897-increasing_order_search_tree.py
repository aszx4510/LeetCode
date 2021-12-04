
# 897. Increasing Order Search Tree

# https://leetcode.com/problems/increasing-order-search-tree/
# https://leetcode.com/problems/increasing-order-search-tree/discuss/165941/Inorder-traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Another method
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if not self.result:  # Leftmost node
                self.result = root
            else:
                self.pre.right = root
            self.pre = root
            self.pre.left = None
            inorder(root.right)

        self.result, self.pre = None, None
        inorder(root)
        return self.result

        # My method, save all nodes

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        nodes = []
        dfs(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        return nodes[0]
