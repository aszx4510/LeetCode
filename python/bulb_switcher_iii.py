
# 1375. Bulb Switcher III

# https://leetcode.com/problems/bulb-switcher-iii/


class Solution(object):
    def numTimesAllBlue(self, light: List[int]) -> int:
        last, result = 0, 0
        for i, l in enumerate(light):
            last = max(last, l)
            if last - 1 == i:
                result += 1
        return result
