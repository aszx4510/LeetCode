
# 598. Range Addition II

# https://leetcode.com/problems/range-addition-ii/description/
# https://discuss.leetcode.com/topic/90720/python-solution-beat-100


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # concise version
        if not ops:
            return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)


        # my version
        min_x, min_y = 40000, 40000
        for x, y in ops:
            min_x = min(x, min_x)
            min_y = min(y, min_y)
        min_x = min(m, min_x)
        min_y = min(n, min_y)
        return min_x * min_y
