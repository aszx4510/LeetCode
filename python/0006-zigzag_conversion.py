
# 6. ZigZag Conversion

# https://leetcode.com/problems/zigzag-conversion/
# https://leetcode.com/problems/zigzag-conversion/solution/
# https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        str_list = [''] * numRows
        current_row = 0
        going_down = False  # First time will trigger current_row == 0  
        for c in s:
            str_list[current_row] += c
            if current_row == 0 or current_row == len(str_list) - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return ''.join(str_list)