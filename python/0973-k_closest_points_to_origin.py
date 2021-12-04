
# 973. K Closest Points to Origin

# https://leetcode.com/problems/k-closest-points-to-origin/
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/217999/JavaC%2B%2BPython-O(N)


class Solution(object):
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points,
            key=lambda x_y: x_y[0] * x_y[0] + x_y[1] * x_y[1])
