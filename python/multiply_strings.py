
# 43. Multiply Strings

# https://leetcode.com/problems/multiply-strings/
# https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        indice = [0] * (m + n)
        # num1[i] * num2[j] = indice[i + j, i + j + 1]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1
                indice_sum = mul + indice[pos2]
                indice[pos1] += indice_sum // 10
                indice[pos2] = indice_sum % 10
        
        result = []
        for number in indice:
            if not (len(result) == 0 and number == 0):
                result.append(str(number))
        return ''.join(result) if len(result) != 0 else '0'
