
# 1359. Count All Valid Pickup and Delivery Options

# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516968/JavaC%2B%2BPython-Easy-and-Concise


class Solution:
    def countOrders(self, n: int) -> int:
        modulo = 1e9 + 7
        ret = 1
        for i in range(2, n + 1):
            ret = ret * (2 * i - 1) * i % modulo
        return int(ret)
