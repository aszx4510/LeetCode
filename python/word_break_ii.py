
# 140. Word Break II

# https://leetcode.com/problems/word-break-ii/
# https://leetcode.com/problems/word-break-ii/solution/
# https://leetcode.com/problems/word-break-ii/discuss/44185/Getting-rid-of-TLE


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(words, dp_index):
            if dp_index == 0:
                result.append(' '.join(words))
                return

            for start, end in dp[dp_index]:
                word = s[start:end]
                dfs([word] + words, start)

        word_set = set(wordDict)
        dp = [[] for _ in range(len(s) + 1)]
        dp[0].append([0])
        for end in range(1, len(dp)):
            temp = []
            for start in range(end):
                word = s[start:end]
                if word in word_set:
                    temp.append([start, end])
            dp[end] = temp

        # Quick check
        if set(Counter(s).keys()) > set(Counter(''.join(wordDict)).keys()):
            return []
        result = []
        dfs([], len(s))

        return result
