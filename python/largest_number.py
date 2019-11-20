
# 179. Largest Number

# https://leetcode.com/problems/largest-number/
# https://leetcode.com/problems/largest-number/discuss/53162/My-3-lines-code-in-Java-and-Python/54346


class Comparable:
    def __init__(self, num):
        self.value = str(num)

    def __lt__(self, other):
        # '82' is before '824' because '82|824' is greater than '824|82'
        return self.value + other.value > other.value + self.value

    def __gt__(self, other):
        return self.value + other.value < other.value + self.value

    def __eq__(self, other):
        return self.value + other.value == other.value + self.value


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(lambda x: Comparable(x), nums))
        str_nums.sort()

        result = ''.join([element.value for element in str_nums]).lstrip('0')
        return '0' if not result else result
