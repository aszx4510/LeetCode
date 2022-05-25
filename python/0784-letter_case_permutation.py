
# 784. Letter Case Permutation

# https://leetcode.com/problems/letter-case-permutation/
# https://leetcode.com/problems/letter-case-permutation/solution/


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]
        
        for c in s:
            n = len(ans)
            if c.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(c.lower())
                    ans[n + i].append(c.upper())
            else:
                for i in range(n):
                    ans[i].append(c)
        return map(''.join, ans)
