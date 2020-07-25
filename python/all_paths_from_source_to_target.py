
# 797. All Paths From Source to Target

# https://leetcode.com/problems/all-paths-from-source-to-target/


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(path):
            if path[-1] == len(graph) - 1:
                result.append(path)
                return

            for node in graph[path[-1]]:
                if node in path:
                    continue
                dfs(path + [node])

        result = []
        dfs([0])
        return result
