
# 72. Edit Distance

# https://leetcode.com/problems/edit-distance/
# http://cpmarkchang.logdown.com/posts/222651-minimum-edit-distance
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1) + 1, len(word2) + 1
        distance = [ [i + j if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        for i in range(1, len(distance)):
            for j in range(1, len(distance[i])):
                distance[i][j] = min(distance[i-1][j] + 1, distance[i][j-1] + 1, (distance[i-1][j-1] + (0 if word1[i - 1] == word2[j - 1] else 1)))
        return distance[-1][-1]
