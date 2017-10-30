
# 532. K-diff Pairs in an Array

# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
# https://discuss.leetcode.com/topic/81714/java-o-n-solution-one-hashmap-easy-to-understand
# https://discuss.leetcode.com/topic/81759/1-liner-in-python-o-n-time


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # concise version for Python
        if k > 0:
            return len(set(nums) & set(num + k for num in nums))
        elif k == 0:
            from collections import Counter
            return sum(count > 1 for count in Counter(nums).values())
        else:
            return 0


        # general solution
        if not nums or k < 0:
            return 0
        record = dict()
        count = 0
        for num in nums:
            record[num] = record.get(num, 0) + 1
        for key, value in record.items():
            if k == 0:
                if value >= 2:
                    count += 1
            else:
                if record.get(key + k, 0) != 0:
                    count += 1
        return count
