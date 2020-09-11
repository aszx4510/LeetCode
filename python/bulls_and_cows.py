
# 299. Bulls and Cows

# https://leetcode.com/problems/bulls-and-cows/
# https://leetcode.com/problems/bulls-and-cows/discuss/74644/Python-3-lines-solution


class Solution:
    def getHint(self, secret, guess):
        s_c, g_c = Counter(secret), Counter(guess)

        a = sum(i == j for i, j in zip(secret, guess))
        b = sum((s_c & g_c).values()) - a
        return f'{a}A{b}B'
