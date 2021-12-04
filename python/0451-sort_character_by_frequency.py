
# 451. Sort Characters By Frequency

# https://leetcode.com/problems/sort-characters-by-frequency/
# https://leetcode.com/problems/sort-characters-by-frequency/discuss/93410/1-line-Python-code.
# https://leetcode.com/problems/sort-characters-by-frequency/discuss/93410/1-line-Python-code./308079


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c * num for c, num in Counter(s).most_common())
