
# 139. Word Break

# https://leetcode.com/problems/word-break/
# https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python/142456


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        max_len = max(map(len, wordDict + ['']))

        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(max(0, i - max_len), i)),
        return ok[-1]


        # # My method, Time Limit Exceeded
        # # This answer maybe right, but cost too much time
        # def helper(pos):
        #     print('in')
        #     if pos == s_len:
        #         return True
        #     if pos > s_len:
        #         return False
        #     for word in wordDict:
        #         print(pos, word)
        #         word_len = len(word)
        #         if pos + word_len > s_len:
        #             continue
        #         else:
        #             if s[pos:pos+word_len] == word:
        #                 result = helper(pos + word_len)
        #                 if result:
        #                     return True
        #     return False

        # if not s:
        #     return False
        
        # wordDict = sorted(wordDict, key=len, reverse=True)
        # s_len = len(s)
        # return helper(0)
