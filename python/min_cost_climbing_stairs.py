
# 746. Min Cost Climbing Stairs

# https://leetcode.com/problems/min-cost-climbing-stairs/description/


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost_sum = [0] * len(cost)
        for i in range(len(cost)):
            if i == 0 or i == 1:
                cost_sum[i] = cost[i]
            else:
                cost_sum[i] = min(cost_sum[i - 2], cost_sum[i - 1]) + cost[i]
        return min(cost_sum[-1], cost_sum[-2])
