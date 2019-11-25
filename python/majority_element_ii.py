
# 229. Majority Element II

# https://leetcode.com/problems/majority-element-ii/
# https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Choose arbitrary numbers
        candidate1, candidate2 = -100, 100
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]
