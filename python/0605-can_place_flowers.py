
# 605. Can Place Flowers

# https://leetcode.com/problems/can-place-flowers/description/


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        continuous_zero = 1  # the edge of flowerbed
        possible_place = 0
        for flower in flowerbed:
            if flower == 1:
                possible_place += max((continuous_zero - 1) // 2, 0)
                continuous_zero = 0
            else:
                continuous_zero += 1
        # the edge of flowerbed
        continuous_zero += 1
        possible_place += max((continuous_zero - 1) // 2, 0)
        return True if possible_place >= n else False
