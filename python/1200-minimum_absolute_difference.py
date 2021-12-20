
# 1200. Minimum Absolute Difference

# https://leetcode.com/problems/minimum-absolute-difference/
# https://leetcode.com/problems/minimum-absolute-difference/solution/


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Counting sort, Time Complexity: O(m + n), only faster in some cases
        min_element, max_element = min(arr), max(arr)
        shift = min_element * -1
        line = [0] * (max_element - min_element + 1)
        ans = []

        for num in arr:
            line[num + shift] = 1

        min_diff = max_element - min_element
        prev = 0
        for curr in range(1, len(line)):
            if not line[curr]:
                continue

            if curr - prev == min_diff:
                ans.append([prev - shift, curr - shift])
            elif curr - prev < min_diff:
                ans = [[prev - shift, curr - prev]]
                min_diff = curr - prev
            prev = curr
        return ans


        # My method, Time Complexity: O(n * logn)
        arr.sort()

        min_diff, ans = float('inf'), []
        for a, b in zip(arr, arr[1:]):
            diff = b - a
            if diff < min_diff:
                min_diff = diff
                ans = [[a, b]]
            elif diff == min_diff:
                ans.append([a, b])
        return ans
