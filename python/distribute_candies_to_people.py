
# 1103. Distribute Candies to People

# https://leetcode.com/problems/distribute-candies-to-people/
# https://leetcode.com/problems/distribute-candies-to-people/discuss/323314/JavaPython3-Easy-code-w-explanation-and-analysis.
# https://leetcode.com/problems/distribute-candies-to-people/discuss/796574/Python-Math-O(k)-solution-with-explanation
# https://leetcode.com/problems/distribute-candies-to-people/discuss/323364/JavaC%2B%2BPython-O(sqrt(candies))-with-explanation


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Time Complexity: O(num_people) (O(k))
        k, n = num_people, candies
        result = [0] * k
        Final = (0, 0)
        for i in range(1, k + 1):
            s = ((-1 - 2 * i) + sqrt(1 + 8 * n)) / (2 * k)
            t = floor(s)
            result[i - 1] = i * (t + 1) + k * t * (t + 1) // 2
            Final = max(Final, (s - floor(s), i))
        result[Final[1] - 1] += (n - sum(result))
        return result

        # result = [0] * num_people
        # x = int(math.sqrt(candies * 2 + 0.25) - 0.5)
        # for i in range(num_people):
        #     m = x // num_people + (x % num_people > i)
        #     result[i] = m * (i + 1) + m * (x + 1) // 2
        # result[x % num_people] += candies - x * (x + 1) // 2
        # return result


        # Implement the simulation, Time Complexity: O(sqrt(candies))
        result = [0] * num_people
        give = 0
        while candies > 0:
            result[give % num_people] += min(candies, give + 1)
            give += 1
            candies -= give
        return result
