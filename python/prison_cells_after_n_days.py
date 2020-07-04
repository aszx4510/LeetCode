
# 957. Prison Cells After N Days

# https://leetcode.com/problems/prison-cells-after-n-days/
# https://leetcode.com/problems/prison-cells-after-n-days/solution/
# https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # Mathematics
        N -= max(N - 1, 0) // 14 * 14
        for i in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells


        N -= max(N - 1, 0) / 14 * 14
        for i in xrange(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells

        # Hash Map for fast-forward
        def next_day():
            new_cells = [0]  # head
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    new_cells.append(1)
                else:
                    new_cells.append(0)
            new_cells.append(0)  # tail
            return new_cells

        seen = dict()
        is_fast_forward = False

        while N > 0:
            if not is_fast_forward:
                state = tuple(cells)
                if state not in seen:
                    seen[state] = N
                else:
                    N %= seen[state] - N
                    is_fast_forward = True

            if N > 0:
                N -= 1
                cells = next_day()

        return cells


        # Bitmap
        def next_day(state_bitmap):
            state_bitmap = ~ (state_bitmap << 1) ^ (state_bitmap >> 1)
            state_bitmap = state_bitmap & 0x7e  # Set head and tail to zero
            return state_bitmap

        seen = dict()
        is_fast_forward = False
        state_bitmap = 0x0
        for cell in cells:  # Initialize bitmap
            state_bitmap <<= 1
            state_bitmap = (state_bitmap | cell)

        while N > 0:
            if not is_fast_forward:
                if state_bitmap not in seen:
                    seen[state_bitmap] = N
                else:
                    N %= seen[state_bitmap] - N
                    is_fast_forward = True

            if N > 0:
                N -= 1
                state_bitmap = next_day(state_bitmap)

        # Convert state_bitmap back to the cells
        result = []
        for i in range(len(cells)):
            result.append(state_bitmap & 0x1)
            state_bitmap >>= 1
        return result[::-1]
