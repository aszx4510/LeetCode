
# 94. Binary Tree Inorder Traversal

# https://leetcode.com/problems/binary-tree-inorder-traversal/
# https://leetcode.com/problems/binary-tree-inorder-traversal/solution/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Stack version
        result = []
        current, stack = root, []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result


        # My method by using stack with lower efficiency
        # if not root:
        #     return []
        # stack = [root]
        # result, temp = [], [[]]
        # while stack:
        #     node = stack.pop()
        #     if node.right:
        #         stack.append(node.right)
        #         temp.append([])
            
        #     temp[-1].append(node.val)

        #     if node.left:
        #         stack.append(node.left)
        #     else:
        #         res = temp.pop()
        #         res.reverse()
        #         result.extend(res)
        # return result
