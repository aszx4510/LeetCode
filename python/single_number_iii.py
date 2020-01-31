
# 260. Single Number III

# https://leetcode.com/problems/single-number-iii/
# https://leetcode.com/problems/single-number-iii/discuss/68901/Sharing-explanation-of-the-solution
# https://leetcode.com/problems/single-number-iii/discuss/68901/Sharing-explanation-of-the-solution/263808
# https://leetcode.com/problems/single-number-iii/discuss/68901/Sharing-explanation-of-the-solution/240646


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res1, res2 = 0, 0
        all_xor = 0
        for num in nums:  # XOR all numbers and get res1 ^ res2
            all_xor ^= num

        # Find rightmost '1'
        for i in range(0, 32):
            if all_xor & (1 << i):
                bit_index = i
                break

        # Get res1 and res2
        for num in nums:
            if num & (1 << bit_index):
                res1 ^= num
        res2 = res1 ^ all_xor
        return [res1, res2]
