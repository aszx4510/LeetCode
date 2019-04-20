
# 95. Unique Binary Search Trees II

# https://leetcode.com/problems/unique-binary-search-trees-ii/
# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31494/A-simple-recursive-solution
# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31494/A-simple-recursive-solution/30203


class Solution(object):
    def generateTrees(self, n: int) -> List[TreeNode]:
        # Recursive version
        def get_tree_list(start, end):
            tree_list = []
            if start > end:
                tree_list.append(None)
            for i in range(start, end + 1):
                left_tree_list = get_tree_list(start, i - 1)
                right_tree_list = get_tree_list(i + 1, end)
                for left in left_tree_list:
                    for right in right_tree_list:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        tree_list.append(root)
            return tree_list

        if n == 0:
            return []
        return get_tree_list(1, n)
