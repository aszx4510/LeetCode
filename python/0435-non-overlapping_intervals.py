
# 435. Non-overlapping Intervals

# https://leetcode.com/problems/non-overlapping-intervals/
# https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python
# https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        erased = 0
        # Sort by the end of each interval
        for temp_start, temp_end in sorted(intervals, key=lambda x: x[1]):
            if temp_start >= end:
                end = temp_end
            else:
                erased += 1
        return erased
