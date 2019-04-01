
# 38. Count and Say

# https://leetcode.com/problems/count-and-say/
# https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions


class Solution:
    def countAndSay(self, n: int) -> str:
        temp = '1'  # It's the first 1
        next_temp = ''
        for i in range(n - 1):  # Start with n=2, run (n - 1) tiems
            j = 0
            while j < len(temp):
                c = temp[j]
                count = 1
                while j + 1 < len(temp) and temp[j] == temp[j + 1]:
                    j += 1
                    count += 1
                next_temp += str(count) + c
                j += 1
            temp = next_temp
            next_temp = ''
        return temp


        # Regex
        # s = '1'
        # for _ in range(n - 1):
        #     s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        # return s
