
# 30-Day LeetCoding Challenge: Week 2 Day 7
# Perform String Shifts

# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        cnt, l = 0, len(s)
        for direction, amount in shift:
            if direction == 0:
                direction = -1
            cnt += direction * amount
        cnt %= l

        if cnt == 0:
            return s
        if cnt < 0:
            cnt += l
        return s[-cnt:] + s[:l - cnt]
