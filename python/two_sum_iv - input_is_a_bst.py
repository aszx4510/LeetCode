
# 653. Two Sum IV - Input is a BST

# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# https://discuss.leetcode.com/topic/98440/java-c-three-simple-methods-choose-one-you-like


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # binary search
        # Time Complexity: O(nlogn), Space Complexity: O(h). h is the height of the tree.
        def dfs(root, current, k):
            if current is None:
                return False
            return search(root, current, k - current.val) or dfs(root, current.left, k) or dfs(root, current.right, k)

        def search(root, current, k):
            if root is None:
                return False
            return (root.val == k and root != current) or (root.val < k and search(root.right, current, k)) or (root.val > k and search(root.left, current, k))

        return dfs(root, root, k)


        # basic version, record value by set
        # Time Complexity: O(n), Space Complexity: O(n).
        value_set = set()        
        def dfs(root, value_set, k):
            if root is None:
                return False
            if k - root.val in value_set:
                return True
            value_set.add(root.val)
            return dfs(root.left, value_set, k) or dfs(root.right, value_set, k)
        return dfs(root, value_set, k)
