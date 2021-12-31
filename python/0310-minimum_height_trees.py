
# 310. Minimum Height Trees

# https://leetcode.com/problems/minimum-height-trees/
# http://web.ntnu.edu.tw/~algo/Tree.html#3
# https://leetcode.com/problems/minimum-height-trees/discuss/1631179/C%2B%2BPython-3-Simple-Solution-w-Explanation-or-Brute-Force-%2B-2x-DFS-%2B-Remove-Leaves-w-BFS
# https://leetcode.com/problems/minimum-height-trees/solution/


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Two DFS to find out diameter
        G, seen = defaultdict(set), [False] * n
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)

        def dfs(i):
            if seen[i]:
                return 0

            longest_path = []
            seen[i] = True
            for adj in G[i]:
                if not seen[adj]:
                    path = dfs(adj)
                    if len(path) > len(longest_path):
                        longest_path = path
            longest_path += [i]
            seen[i] = False
            return longest_path

        path = dfs(dfs(0)[0])
        return set([path[len(path) // 2], path[(len(path) - 1) // 2]])  # Middle points


        # Remove leaves using BFS
        if n <= 2:
            return [i for i in range(n)]

        neighbors = [set() for _ in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                # Remove the edge
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
        return leaves
