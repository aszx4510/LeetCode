
# 165. Compare Version Numbers

# https://leetcode.com/problems/compare-version-numbers/
# https://leetcode.com/problems/compare-version-numbers/discuss/50774/Accepted-small-Java-solution.


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Another more concise solution
        version1, version2 = version1.split('.'), version2.split('.')
        max_len = max(len(version1), len(version2))

        for i in range(max_len):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0
            if v1 == v2:
                continue
            return 1 if v1 > v2 else -1
        return 0


        # My method, it also works
        version1, version2 = version1.split('.'), version2.split('.')

        # Set v1 is the longer one
        swap_flag = False
        if len(version1) < len(version2):
            version1, version2 = version2, version1
            swap_flag = True

        v1_len, v2_len = len(version1), len(version2)
        for v1, v2 in zip(version1, version2):
            if int(v1) > int(v2):
                return 1 if not swap_flag else -1
            elif int(v1) < int(v2):
                return -1 if not swap_flag else 1

        while v1_len > v2_len:
            if int(version1[v2_len]) != 0:
                return 1 if not swap_flag else -1
            v2_len += 1

        return 0
