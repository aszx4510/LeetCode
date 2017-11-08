
# 566. Reshape the Matrix

# https://leetcode.com/problems/reshape-the-matrix/description/
# https://discuss.leetcode.com/topic/87899/python-solutions
# https://stupidpythonideas.blogspot.tw/2013/08/how-grouper-works.html


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat_list = [item for sublist in nums for item in sublist]
        print(flat_list)
        if len(flat_list) != r * c:
            return nums
        tuples = zip(*([iter(flat_list)] * c))
        return list(map(list, tuples))
