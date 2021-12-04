
# 89. Gray Code

# https://leetcode.com/problems/gray-code/
# https://leetcode.com/problems/gray-code/discuss/29891/Share-my-solution
# https://leetcode.com/problems/gray-code/discuss/29891/Share-my-solution/158437


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            size = len(result)
            for k in range(size - 1, -1, -1):
                result.append(result[k] | 1 << i)  # bit-wise or operator
        return result
