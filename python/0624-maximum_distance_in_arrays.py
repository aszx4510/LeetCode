
# 624. Maximum Distance in Arrays

# https://leetcode.com/problems/maximum-distance-in-arrays/
# https://leetcode.com/problems/maximum-distance-in-arrays/solution/
# https://leetcode.com/problems/maximum-distance-in-arrays/discuss/1629609/Python-100-runtime


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Single Scan, Time Complexity: O(n)
        ans = 0
        min_val, max_val = arrays[0][0], arrays[0][-1]

        for array in arrays[1:]:
            ans = max(
                ans,
                array[-1] - min_val,
                max_val - array[0]
            )

            min_val = min(min_val, array[0])
            max_val = max(max_val, array[-1])
        return ans


        # Another version
        global_min, index_min = min((array[0], index) for index, array in enumerate(arrays))
        global_max, index_max = max((array[-1], index) for index, array in enumerate(arrays))

        if index_min != index_max:
            return global_max - global_min

        second_min = min(array[0] for index, array in enumerate(arrays) if index != index_min)
        second_max = max(array[-1] for index, array in enumerate(arrays) if index != index_max)
        return max(global_max - second_min, second_max - global_min)
