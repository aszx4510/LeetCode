
# 1345. Jump Game IV

# https://leetcode.com/problems/jump-game-iv/
# https://leetcode.com/problems/jump-game-iv/solution/


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)

        # Biderectinal Breadth-First Search
        curr_layer = [0]
        visited, other = set([0, n - 1]), set([n - 1])
        step = 0

        while curr_layer:
            if len(curr_layer) > len(other):
                curr_layer, other = other, curr_layer

            next_layer = set()
            for node in curr_layer:
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        next_layer.add(child)

                graph[arr[node]].clear()

                # Neighbors
                for child in [node - 1, node + 1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        next_layer.add(child)

            curr_layer = next_layer
            step += 1
        return -1


        # # Breadth-First Search, Time Limit Exceeded
        # curr_layer = [0]
        # visited = set()
        # step = 0
        # while curr_layer:
        #     next_layer = list()

        #     for node in curr_layer:
        #         if node == n - 1:
        #             return step

        #         for child in graph[arr[node]]:
        #             if child not in visited:
        #                 visited.add(child)
        #                 next_layer.append(child)

        #         graph[arr[node]].clear()

        #         # Neighbors
        #         for child in [node - 1, node + 1]:
        #             if 0 <= child < n and child not in visited:
        #                 visited.add(child)
        #                 next_layer.append(child)

        #     curr_layer = next_layer
        #     step += 1
        # return -1
