
# 163. Missing Ranges

# https://leetcode.com/problems/missing-ranges/
# https://leetcode.com/problems/missing-ranges/discuss/50631/Ten-line-python-solution


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # Concise version
        nums = [lower - 1] + nums + [upper + 1]
        result = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                result.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:
                result.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))
        return result


        # My method
        current = lower
        result = []
        for num in nums:
            if num < current:
                continue
            elif num == current:
                current += 1
            else:
                if num - 1 == current:
                    result.append(str(current))
                else:
                    result.append(str(current) + '->' + str(num - 1))
                current = num + 1
        if current <= upper:
            if upper == current:
                result.append(str(current))
            else:
                result.append(str(current) + '->' + str(upper))
        return result
