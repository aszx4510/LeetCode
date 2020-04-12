
# 1046. Last Stone Weight

# https://leetcode.com/problems/last-stone-weight/
# https://leetcode.com/problems/last-stone-weight/discuss/575360/Python3-Heapq-(Priority-Queue)

# There still some ways to do max heap by using heapq
# https://stackoverflow.com/questions/12681772/pop-max-value-from-a-heapq-python-is-there-a-max-heap-in-python


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1 <= stones[i] <= 1000
        negative_stones = [-weight for weight in stones]
        heapq.heapify(negative_stones)
        
        while len(negative_stones) > 1:
            # print(negative_stones)
            min1, min2 = heapq.heappop(negative_stones), heapq.heappop(negative_stones)
            diff = min1 - min2
            # print(min1, min2, diff)
            if diff:
                heapq.heappush(negative_stones, diff)
        return heapq.heappop(negative_stones) * -1 if len(negative_stones) == 1 else 0
