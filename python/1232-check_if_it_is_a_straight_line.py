
# 1232. Check If It Is a Straight Line

# https://leetcode.com/problems/check-if-it-is-a-straight-line/


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        def cross_product(v1, v2):
            return v1[0] * v2[1] - v2[0] * v1[1]
        v1 = tuple(x1 - x2 for x1, x2 in zip(coordinates[1], coordinates[0]))
        for i in range(2, len(coordinates)):
            v2 = tuple(x1 - x2 for x1,
                       x2 in zip(coordinates[i], coordinates[0]))
            if cross_product(v1, v2):
                return False
        return True
