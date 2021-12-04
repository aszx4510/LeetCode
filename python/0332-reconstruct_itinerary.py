
# 332. Reconstruct Itinerary

# https://leetcode.com/problems/reconstruct-itinerary/
# https://leetcode.com/problems/reconstruct-itinerary/solution/
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # http://www.csie.ntnu.edu.tw/~u91029/Circuit.html#3
        # Hierholzer's Algorithm
        def dfs(origin):
            dest_list = flight_map[origin]
            while dest_list:
                next_dest = dest_list.pop()
                dfs(next_dest)
            result.append(origin)

        flight_map = defaultdict(list)
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            flight_map[origin].append(dest)

        for origin, dest_list in flight_map.items():
            dest_list.sort(reverse=True)

        result = []
        dfs('JFK')

        return result[::-1]
