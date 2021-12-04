
# 207. Course Schedule

# https://leetcode.com/problems/course-schedule/
# https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Find out the ring(cycle)
        # if node v has not been visited, then mark it as 0.
        # if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
        # if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in pres[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True

        pres = [ [] for _ in range(numCourses)]
        for (course, pre) in prerequisites:
            pres[pre].append(course)

        visited = [0] * numCourses
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
