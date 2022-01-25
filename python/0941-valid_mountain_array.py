
# 941. Valid Mountain Array

# https://leetcode.com/problems/valid-mountain-array/
# https://leetcode.com/problems/valid-mountain-array/solution/
# https://leetcode.com/problems/valid-mountain-array/discuss/194900/C%2B%2BJavaPython-Climb-Mountain


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Two pointer
        i, j, n = 0, len(n) - 1, len(n)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1
        return 0 < i == j < n - 1


        # Concise version
        i, n = 0, len(arr)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        # Peek can't be first or last
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1


        # My version
        up_flag, down_flag = None, None
        for prev, curr in zip(arr, arr[1:]):
            if prev < curr:
                if up_flag is None:
                    up_flag = True
                elif not up_flag:
                    return False
            if prev > curr:
                if up_flag and down_flag is None:
                    up_flag, down_flag = False, True
                elif not up_flag and not down_flag:
                    return False
            if prev == curr:
                return False
        return up_flag is not None and down_flag is not None and not up_flag and down_flag
