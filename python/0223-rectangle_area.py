
# 223. Rectangle Area

# https://leetcode.com/problems/rectangle-area/
# https://leetcode.com/problems/rectangle-area/discuss/62139/Python-concise-solution.


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # Concise version
        overlap = max(0, min(G, C) - max(A, E)) * max(0, min(H, D) - max(F, B))
        return (C - A) * (D - B) + (G - E) * (H - F) - overlap


        # My method
        # Get the interval from [a, b] and [c, d]
        def get_interval_length(a, b, c, d):
            # print(a, b, c, d)
            if a <= c <= b and a <= d <= b:
                return d - c
            elif c <= a <= d and c <= b <= d:
                return b - a
            elif a <= c <= b:
                return b - c
            elif c <= a <= d:
                return d - a
            return 0
        x = get_interval_length(A, C, E, G)
        y = get_interval_length(B, D, F, H)
        rec1 = (C - A) * (D - B)
        rec2 = (G - E) * (H - F)
        cover = x * y
        return rec1 + rec2 - cover
