
# 394. Decode String

# https://leetcode.com/problems/decode-string/
# https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack


class Solution:
    def decodeString(self, s: str) -> str:
        # Concise version
        stack = []
        num, string = 0, ''

        for c in s:
            if c == '[':
                stack.append(string)
                stack.append(num)
                num, string = 0, ''
            elif c == ']':
                prev_num, prev_string = stack.pop(), stack.pop()
                string = prev_string + prev_num * string
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                string += c
        return string


        # My method
        stack, digit_stack = [], []
        digit_flag, push_flag = False, False
        result = ''
        for c in s:
            if c.isdigit():
                if not digit_flag:
                    digit_stack.append(int(c))
                else:
                    digit_stack.append(digit_stack.pop() * 10 + int(c))
                digit_flag = True
            elif c.isalpha():
                if push_flag:
                    stack.append((digit_stack.pop(), c))
                elif not push_flag and stack:
                    peak_digit, peak_alpha = stack.pop()
                    stack.append((peak_digit, peak_alpha + c))
                else:  # Last string
                    result += c
                digit_flag, push_flag = False, False
            elif c == '[':
                push_flag = True
                digit_flag = False
            elif c == ']':
                peak_digit, peak_alpha = stack.pop()
                temp_result = peak_alpha * peak_digit
                if digit_stack:
                    stack.append((digit_stack.pop(), temp_result))
                elif stack:
                    peak_digit, peak_alpha = stack.pop()
                    stack.append((peak_digit, peak_alpha + temp_result))
                else:
                    result += temp_result
                digit_flag, push_flag = False, False
        return result
