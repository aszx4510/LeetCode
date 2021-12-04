
# 1376. Time Needed to Inform All Employees

# https://leetcode.com/problems/time-needed-to-inform-all-employees/


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(head, time):
            for i in tree[head]:
                dfs(i, time + informTime[head])
            result[0] = max(result[0], time)

        # Build the tree
        tree = collections.defaultdict(list)
        for i in range(n):
            if manager[i] == -1:
                continue
            tree[manager[i]].append(i)

        result = [0]
        dfs(headID, 0)
        return result[0]
