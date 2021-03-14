
# 599. Minimum Index Sum of Two Lists

# https://leetcode.com/problems/minimum-index-sum-of-two-lists/


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum, result = float('inf'), []
        rest_index = {rest_name: i for i, rest_name in enumerate(list1)}

        for i, rest_name in enumerate(list2):
            if rest_name not in rest_index:
                continue

            temp = i + rest_index[rest_name]
            if temp == min_sum:
                result.append(rest_name)
            elif temp < min_sum:
                result = [rest_name]
                min_sum = temp

        return result
