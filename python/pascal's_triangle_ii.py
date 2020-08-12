
# 119. Pascal's Triangle II

# https://leetcode.com/problems/pascals-triangle-ii/description/
# https://discuss.leetcode.com/topic/15559/very-simple-python-solution


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [0] * (rowIndex + 1)
        result[0] += 1
        for i in range(rowIndex + 1):
            for j in range(i, 0, -1):
                result[j] += result[j - 1]
        return result


        # solve by using list comprehension but not O(k) extra space
        result = [1]
        for i in range(rowIndex):
            result = [x + y for x, y in zip([0] + result, result + [0])]
        return result
