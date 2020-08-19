
# 824. Goat Latin

# https://leetcode.com/problems/goat-latin/


class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = list('aeiou')

        result = []
        for i, token in enumerate(S.split(' '), start=1):
            if token[0].lower() not in vowels:
                token = token[1:] + token[:1]
            result.append(token + 'ma' + ('a' * i))
        return ' '.join(result)
