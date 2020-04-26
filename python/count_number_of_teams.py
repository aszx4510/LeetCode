
# 1395. Count Number of Teams

# https://leetcode.com/problems/count-number-of-teams/
# https://leetcode.com/problems/count-number-of-teams/discuss/554918/Python-Easy-O(N2)-DP-solution


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        greater = defaultdict(int)
        lesser = defaultdict(int)
        count = 0

        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    lesser[i] += 1

        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    count += greater[j]
                else:
                    count += lesser[j]
        return count


        # # My method
        # def combination(n):
        #     return n * (n - 1) // 2 if n > 1 else 0

        # def get_ijk_result(rating_list):
        #     exists = [0] * 100001
        #     increasing = [0] * 100001
        #     result = 0
        #     for rate in rating_list:
        #         increasing[rate] = sum(exists[:rate])
        #         result += sum(increasing[:rate])

        #         exists[rate] = 1
        #     return result

        # return get_ijk_result(rating) + get_ijk_result(rating[::-1])
