
# 886. Possible Bipartition

# https://leetcode.com/problems/possible-bipartition/
# https://leetcode.com/problems/possible-bipartition/discuss/159009/Python-DFS-with-explanation
# https://leetcode.com/problems/possible-bipartition/discuss/159009/Python-DFS-with-explanation/556440


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # DFS: group_1 -> group_2 -> gropu_1 -> group_2 -> ....
        def visit(num, depth):
            if num in depths:
                return (depth - depths[num]) % 2 == 0

            depths[num] = depth
            return all(visit(v, depth + 1) for v in dis[num])

        depths = {}  # Record the depth in the tree for each element
        dis = defaultdict(set)
        for u, v in dislikes:
            dis[u].add(v)
            dis[v].add(u)

        return all(u in depths or visit(u, 0) for u in dis)
