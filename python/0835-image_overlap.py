
# 835. Image Overlap

# https://leetcode.com/problems/image-overlap/
# https://leetcode.com/problems/image-overlap/discuss/150504/Python-Easy-Logic


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        diff = defaultdict(int)
        a, b = [], []

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    a.append((i, j))
                if B[i][j]:
                    b.append((i, j))

        result = 0
        for t1 in a:
            for t2 in b:
                t3 = (t1[0] - t2[0], t1[1] - t2[1])
                diff[t3] += 1
                result = max(result, diff[t3])

        return result
