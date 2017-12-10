
# 728. Self Dividing Numbers

# https://leetcode.com/problems/self-dividing-numbers/description/


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = list()
        for num in range(left, right + 1):
            remain = num
            while remain > 0:
                mod = remain % 10
                if mod == 0 or num % mod != 0:
                    break
                remain = remain // 10
            if remain == 0:
                ans.append(num)
        return ans
