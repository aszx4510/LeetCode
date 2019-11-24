
# 220. Contains Duplicate III

# https://leetcode.com/problems/contains-duplicate-iii/
# https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        buckets = {}
        w = t + 1
        for i in range(0, len(nums)):
            m = nums[i] // w
            if m in buckets:
                return True
            if m + 1 in buckets and abs(nums[i] - buckets[m + 1]) < w:
                return True
            if m - 1 in buckets and abs(nums[i] - buckets[m - 1]) < w:
                return True

            buckets[m] = nums[i]
            if i >= k:
                del buckets[nums[i - k] // w]
        return False
