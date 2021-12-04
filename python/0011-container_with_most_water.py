
# 11. Container With Most Water

# https://leetcode.com/problems/container-with-most-water/
# https://leetcode.com/problems/container-with-most-water/solution/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while right > left:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area
