
# 1017. Convert to Base -2

# https://leetcode.com/contest/weekly-contest-130/problems/convert-to-base-2/


class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        # Convert to base 2
        binary = []
        while N > 0:
            binary.append(N % 2)
            N //= 2

        # Convert to base -2
        i, odd = 0, False
        while i < len(binary):
            if odd and binary[i] == 1:
                if i + 1 >= len(binary):
                    binary.append(0)
                binary[i + 1] += 1

            if binary[i] == 2:
                if i + 1 >= len(binary):
                    binary.append(0)
                binary[i] = 0
                binary[i + 1] += 1
            odd = not odd
            i += 1

        # Output result
        binary.reverse()
        binary = list(map(str, binary))
        binary = ''.join(binary)
        return binary
