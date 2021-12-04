
# 1011. Capacity To Ship Packages Within D Days

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # Exactly same as #410
        def is_valid(target):
            split, total = 1, 0
            for weight in weights:
                total += weight
                if total > target:
                    total = weight
                    split += 1
                    if split > D:
                        return False
            return True

        left, right = max(weights), sum(weights)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
