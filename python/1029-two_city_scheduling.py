
# 1029. Two City Scheduling

# https://leetcode.com/problems/two-city-scheduling/


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        sorted_diff = sorted(((c_a - c_b, i)
                              for i, (c_a, c_b) in enumerate(costs)))
        a_index, b_index = [i for _, i in sorted_diff[: n]], [
            i for _, i in sorted_diff[n:]]
        return sum(costs[i][0] for i in a_index) + sum(costs[i][1] for i in b_index)
