
# 1044. Longest Duplicate Substring

# https://leetcode.com/problems/longest-duplicate-substring/
# https://leetcode.com/problems/longest-duplicate-substring/discuss/290871/Python-Binary-Search
# https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/Python-Binary-search-O(n-log-n)-average-with-Rabin-Karp-explained


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = pow(2, 63) - 1

        def verify(L):
            # Rabin-Karp Algorithm, slide window for length L
            p = pow(26, L, mod)

            # https://stackoverflow.com/questions/24463202/typeerror-get-takes-no-keyword-arguments
            # a lot of built-in functions and methods don't actually have names for their arguments.
            curr = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {curr}

            for i in range(L, len(S)):
                curr = (curr * 26 + A[i] - (A[i - L] * p)) % mod
                if curr in seen:
                    return i - L + 1
                seen.add(curr)
            return None

        res = 0
        left, right = 0, len(S)

        # Binary search for the length of substring
        while left < right:
            mid = (left + right + 1) // 2  # Round up
            pos = verify(mid)

            if pos:
                left = mid
                res = pos
            else:
                right = mid - 1
        return S[res: res + left]
