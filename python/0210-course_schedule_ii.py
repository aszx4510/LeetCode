
# 210. Course Schedule II

# https://leetcode.com/problems/course-schedule-ii/
# https://alrightchiu.github.io/SecondRound/graph-li-yong-dfsxun-zhao-dagde-topological-sorttuo-pu-pai-xu.html
# https://www.geeksforgeeks.org/topological-sorting/
# https://www.youtube.com/watch?v=Q9PIxaNGnig
# https://leetcode.com/problems/course-schedule-ii/discuss/59455/Fast-python-DFS-solution-with-inline-explanation


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs_can_finish(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in graph[i]:
                if not dfs_can_finish(j):
                    return False
            visited[i] = 1
            return True

        def dfs(i):
            if visited[i]:
                return False
            visited[i] = True
            for pre in graph[i]:
                if visited[pre]:
                    continue
                dfs(pre)
            stack.insert(0, i)

        graph = [ [] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        # Check it can be finished
        # Reference to #207
        visited = [0] * numCourses
        for i in range(numCourses):
            if not dfs_can_finish(i):
                return []

        # Reset the visited
        visited = [False] * numCourses
        stack = []
        for i in range(numCourses):
            if visited[i]:
                continue
            dfs(i)
        return stack
