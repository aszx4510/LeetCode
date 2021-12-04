
# 983. Minimum Cost For Tickets

# https://leetcode.com/problems/minimum-cost-for-tickets/
# https://leetcode.com/problems/minimum-cost-for-tickets/discuss/228421/Python-solution


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Concise version
        pass_1_day, pass_7_day, pass_30_day = costs[0], costs[1], costs[2]
        result = [0] * (days[-1] + 1)

        for i in range(len(result)):
            if i not in days:
                result[i] = result[i - 1]
            else:
                today_cost = result[max(0, i - 1)] + pass_1_day
                day7_cost = result[max(0, i - 7)] + pass_7_day
                day30_cost = result[max(0, i - 30)] + pass_30_day

                result[i] = min(today_cost, day7_cost, day30_cost)
        return result[-1]


        # My version
        pass_1_day, pass_7_day, pass_30_day = costs[0], costs[1], costs[2]
        
        result = []
        for day in days:
            while len(result) <= day:
                if len(result) == 0:
                    result.append(0)
                    continue

                today_cost = result[-1] + (pass_1_day if len(result) == day else 0)
                day7_cost = result[-7] + pass_7_day if len(result) >= 7 else pass_7_day
                day30_cost = result[-30] + pass_30_day if len(result) >= 30 else pass_30_day

                result.append(min(today_cost, day7_cost, day30_cost))
        return result[-1]
