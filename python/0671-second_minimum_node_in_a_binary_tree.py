
# 671. Second Minimum Node In a Binary Tree

# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
# https://discuss.leetcode.com/topic/102097/python-extremely-easy-to-understand-beats-91


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
        second = [float('inf')]

        def dfs(node):
            if node is None:
                return
            if root.val < node.val < second[0]:
                second[0] = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return -1 if second[0] == float('inf') else second[0]
