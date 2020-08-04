
# 852. Peak Index in a Mountain Array

# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139840/JavaPython-3-O(n)-and-O(log(n))-codes


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # Time Complexity: O(logn)
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


        # Time Complexity: O(n)
        for i in range(1, len(A)):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                return i
        return -1
