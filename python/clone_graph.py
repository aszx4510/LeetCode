
# 133. Clone Graph

# https://leetcode.com/problems/clone-graph/
# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).
# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively)./263488


"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs_clone(node_origin):
            if not node_origin:
                return None
            node_clone = Node(node_origin.val, [])
            visited_nodes[node_origin] = node_clone
            for neighbor in node_origin.neighbors:
                if neighbor in visited_nodes:
                    visited_nodes[node_origin].neighbors.append(visited_nodes[neighbor])
                else:
                    visited_nodes[node_origin].neighbors.append(dfs_clone(neighbor))
            return node_clone

        visited_nodes = {}
        return dfs_clone(node)
