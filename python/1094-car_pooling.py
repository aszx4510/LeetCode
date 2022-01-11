
# 1094. Car Pooling

# https://leetcode.com/problems/car-pooling/
# https://leetcode.com/problems/car-pooling/solution/


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Another version
        timestamp = [0] * 1001
        for passengers, s, e in trips:
            timestamp[s] += passengers
            timestamp[e] -= passengers

        curr = 0
        for i in range(len(timestamp)):
            curr += timestamp[i]
            if curr > capacity:
                return False
        return True


        # My method
        start, end = [0] * 1001, [0] * 1001
        for passengers, s, e in trips:
            start[s] += passengers
            end[e] -= passengers

        curr = 0
        for i in range(len(start)):
            curr += start[i] + end[i]
            if curr > capacity:
                return False
        return True
