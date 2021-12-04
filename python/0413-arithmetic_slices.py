
# 413. Arithmetic Slices

# https://leetcode.com/problems/arithmetic-slices/
# https://leetcode.com/problems/arithmetic-slices/discuss/90112/Python-DP-solution/94658


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # Elegant method
        curr, ans = 0, 0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                curr += 1
                ans += curr
            else:
                curr = 0
        return ans
        

        # My method
        ans = 0
        layer = []
        for i in range(len(A) - 2):
            layer.append(1 if A[i] - A[i+1] == A[i+1] - A[i+2] else 0)
        ans += sum(layer)

        while len(layer) > 1 and sum(layer):
            layer = list(map(lambda x,y: 1 if x and y else 0, layer[:-1], layer[1:]))
            ans += sum(layer)
        return ans
