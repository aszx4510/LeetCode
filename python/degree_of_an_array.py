
# 697. Degree of an Array

# https://leetcode.com/problems/degree-of-an-array/description/
# https://discuss.leetcode.com/topic/107124/python-easy-and-concise-solution


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # copy from submissions
        nums_dict = dict()
        for i in range(len(nums)):
            current = nums[i]
            if current in nums_dict:
                nums_dict[current][1] = i  # last happening
                nums_dict[current][2] += 1
            else:
                nums_dict[current] = [i, i, 1]
        max_count = -1
        min_length = None
        for first, last, count in nums_dict.values():
            if count > max_count:
                max_count = count
                min_length = last - first + 1
            elif count == max_count:
                min_length = min(last - first + 1, min_length)
        return min_length


        # concise version
        # https://discuss.leetcode.com/topic/107124/python-easy-and-concise-solution
        import collections
        c = collections.Counter(nums)
        first, last = {}, {}
        for index, num in enumerate(nums):
            first.setdefault(num, index)
            last[num] = index
        degree = max(c.values())  # max frequency
        return min(last[num] - first[num] + 1 for num in c if c[num] == degree)


        # my version
        count_dict = dict()
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        max_count, max_list = -1, list()
        for num, count in count_dict.items():
            if count > max_count:
                max_count = count
                max_list = [num]
            elif count == max_count:
                max_list.append(num)

        position = dict()
        for i in range(len(nums)):
            if nums[i] in max_list:
                position.setdefault(nums[i], []).append(i)

        min_degree = 99999  # max is 50000
        for num, pos in position.items():
            degree = pos[-1] - pos[0] + 1
            min_degree = min(degree, min_degree)
        return min_degree
