
# 986. Interval List Intersections

# https://leetcode.com/problems/interval-list-intersections/
# https://leetcode.com/problems/interval-list-intersections/discuss/231532/Python3-Really-easy-concept%3A-Overlapping


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i][0] <= B[j][1] and B[j][0] <= A[i][1]:
                result.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return result
