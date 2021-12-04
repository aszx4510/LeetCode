
# 371. Sum of Two Integers

# https://leetcode.com/problems/sum-of-two-integers/
# https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed
# https://leetcode.com/problems/sum-of-two-integers/discuss/353429/Java-2ms-accepted-solution-use-bit-manipulation-without-trick
# https://www.youtube.com/watch?v=Pi7sMZWIIXE

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits max integer
        MAX = 0x7FFFFFFF
        # # 32 bits min integer (just a note)
        # MIN = 0x80000000

        # Mask to get last 32 bits
        # Cause Python can handle numbers which are larger than 32 bits, 
        # So we need to simulate 32 bits integers by mask
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(a, b)
        # If a is negative, get a's 32 bits complement positive first,
        # then get 32-bit positive's Python complement negative
        print(a)
        return a if a <= MAX else ~(a ^ mask)


        # # Java version
        # # Can not handle 2^31(integer) in Python
        # def decrease(a, b):
        #     print('enter decrease', a, b)
        #     if a == b: return 0
        #     if a == 0:
        #         return -1 * b
        #     if b == 0:
        #         return a
        #     if a < b:
        #         return -1 * decrease(b, a)
        #     decrease_without_carry = a ^ b
        #     decrease_carry = ((~a) & b) << 1
        #     return decrease(decrease_without_carry, decrease_carry)

        # if a == 0: return b
        # if b == 0: return a
        # if a < 0 and b < 0:
        #     return -1 * self.getSum(-a, -b)
        # if a < 0:
        #     return -1 * decrease(-a, b)
        # if b < 0:
        #     return -1 * decrease(a, -b)
        # sum_without_carry = a ^ b
        # carry = (a & b) << 1
        # return self.getSum(sum_without_carry, carry)


        # # Simple case:
        # # Can not support negative number
        # while b != 0:
        #     carry = (a & b) << 1
        #     a = a ^ b
        #     b = carry
        # return a
