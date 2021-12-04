
# 228. Summary Ranges

# https://leetcode.com/problems/summary-ranges/
# https://leetcode.com/problems/summary-ranges/discuss/63193/6-lines-in-Python


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Concise version
        ranges = []
        for n in nums:
            print(ranges)
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,  # the comma is very important
        return ['->'.join(map(str, r)) for r in ranges]


        # My method
        def append_result(start, end):
            if not end:
                result.append(str(start))
            else:
                result.append(str(start) + '->' + str(end))

        if not nums:
            return []
        result = []
        start, end = None, None
        for num in nums:
            if start is None:
                start = num
            elif start is not None and end is None and num - start == 1:
                end = num
            elif start is not None and end and num - end == 1:
                end = num
            else:
                append_result(start, end)
                start, end = num, None
        append_result(start, end)
        return result
