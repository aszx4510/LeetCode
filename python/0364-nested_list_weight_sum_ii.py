
# 364. Nested List Weight Sum II

# https://leetcode.com/problems/nested-list-weight-sum-ii/
# https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83641/No-depth-variable-no-multiplication


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # Concise version, without depth variable
        curr_lvl, next_lvl = [nestedList], []
        weighted_sum, unweighted_sum = 0, 0

        while curr_lvl:
            for nl in curr_lvl:
                for ni in nl:
                    if ni.isInteger():
                        unweighted_sum += ni.getInteger()
                    else:
                        next_lvl.append(ni.getList())
            curr_lvl, next_lvl = next_lvl, []
            weighted_sum += unweighted_sum
        return weighted_sum


        # My method
        lvl, lvl_dict = 0, {}
        curr_lvl, next_lvl = [nestedList], []

        while curr_lvl:

            lvl_sum = 0
            for nl in curr_lvl:
                for ni in nl:
                    if ni.isInteger():
                        lvl_sum += ni.getInteger()
                    else:
                        next_lvl.append(ni.getList())

            lvl_dict[lvl] = lvl_sum

            curr_lvl, next_lvl = next_lvl, []
            lvl += 1

        max_depth = max(lvl_dict.keys()) + 1
        return sum([(max_depth - lvl) * lvl_sum for lvl, lvl_sum in lvl_dict.items()])
