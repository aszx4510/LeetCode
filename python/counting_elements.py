
# 30-Day LeetCoding Challenge: Week 1 Day 7
# Counting Elements

# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/


class Solution:
    def countElements(self, arr: List[int]) -> int:
        counting = [0] * 1001  # 0 <= arr[i] <= 1000
        for ele in arr:
            counting[ele] += 1
        
        result = 0
        for i in range(1, len(counting)):
            if counting[i]:
                result += counting[i - 1]
        return result
