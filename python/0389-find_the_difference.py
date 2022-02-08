
# 389. Find the Difference

# https://leetcode.com/problems/find-the-difference/
# https://leetcode.com/problems/find-the-difference/solution/
# https://leetcode.com/problems/find-the-difference/discuss/86904/3-Different-Python-Solutions-(Dictionary-Difference-XOR)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(s)
        for ch in t:
            if ch not in counter or counter[ch] == 0:
                return ch
            else:
                counter[ch] -= 1


        # XOR
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)


        # Another method
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)
