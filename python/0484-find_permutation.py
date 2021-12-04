
# 484. Find Permutation

# https://leetcode.com/problems/find-permutation/
# https://leetcode.com/problems/find-permutation/discuss/96624/1-liner-and-5-liner-visual-explanation


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result = list(range(1, len(s) + 2))
        for m in re.finditer('D+', s):
            i, j = m.start(), m.end() + 1
            result[i:j] = result[i:j][::-1]
        return result
