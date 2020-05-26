
# 410. Split Array Largest Sum

# https://leetcode.com/problems/split-array-largest-sum/
# https://leetcode.com/problems/split-array-largest-sum/solution/
# https://leetcode.com/problems/split-array-largest-sum/discuss/89817/Clear-Explanation%3A-8ms-Binary-Search-Java
# https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Exactly same as #1011
        def is_valid(target):
            split, total = 1, 0
            for num in nums:
                total += num
                if total > target:
                    total = num
                    split += 1
                    if split > m:
                        return False
            return True

        left, right = max(nums), sum(nums)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
