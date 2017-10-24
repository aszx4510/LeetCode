
# 414. Third Maximum Number

# https://leetcode.com/problems/third-maximum-number/description/
# https://discuss.leetcode.com/topic/70613/intuitive-and-short-python-solution


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # concise version
        max_list = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num in max_list:
                continue
            if num > max_list[0]:
                max_list = [num, max_list[0], max_list[1]]
            elif num > max_list[1]:
                max_list = [max_list[0], num, max_list[1]]
            elif num > max_list[2]:
                max_list = [max_list[0], max_list[1], num]
        return max_list[2] if float('-inf') not in max_list else max_list[0]


        # my first version
        max_list = [None, None, None]
        for num in nums:
            if num in max_list:
                continue
            if max_list[0] is None or num > max_list[0]:
                max_list[2] = max_list[1]
                max_list[1] = max_list[0]
                max_list[0] = num
                continue
            if max_list[1] is None or num > max_list[1]:
                max_list[2] = max_list[1]
                max_list[1] = num
                continue
            if max_list[2] is None or num > max_list[2]:
                max_list[2] = num
                continue
        return max_list[0] if None in max_list else max_list[2]
        # if None in max_list:
        #     return max_list[0]
        # else:
        #     return max_list[2]
