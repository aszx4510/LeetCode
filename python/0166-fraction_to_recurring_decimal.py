
# 166. Fraction to Recurring Decimal

# https://leetcode.com/problems/fraction-to-recurring-decimal/
# https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51106/My-clean-Java-solution


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        result_list = []

        # Check positive or negative
        pos_num, pos_don = numerator >= 0, denominator >= 0
        result_list.append('-' if pos_num != pos_don else '')
        numerator, denominator = abs(numerator), abs(denominator)

        # Integral section
        result_list.append(str(numerator // denominator))
        numerator %= denominator
        if numerator == 0:
            return ''.join(result_list)

        # Fractional section
        result_list.append('.')
        divide_mapping = {}
        divide_mapping[numerator] = len(result_list)
        while numerator != 0:
            numerator *= 10
            result_list.append(str(numerator // denominator))
            numerator %= denominator

            if numerator in divide_mapping:
                result_list.insert(divide_mapping[numerator], '(')
                result_list.append(')')
                break
            else:
                divide_mapping[numerator] = len(result_list)

        return ''.join(result_list)
