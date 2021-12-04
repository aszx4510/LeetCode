
# 1344. Angle Between Hands of a Clock

# https://leetcode.com/problems/angle-between-hands-of-a-clock/


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_ratio = minutes / 60
        hr_ratio = (hour % 12) / 12
        m = 360 * min_ratio
        h = 360 * hr_ratio + (360 / 12 * min_ratio)

        result = abs(m - h) if abs(m - h) <= 180 else abs(abs(m - h) - 360)
        return result
