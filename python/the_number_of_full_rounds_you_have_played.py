
# 1904. The Number of Full Rounds You Have Played

# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/
# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/discuss/1284279/Python3-math-ish


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        start_hour, start_minute = (int(s) for s in startTime.split(':'))
        end_hour, end_minute = (int(s) for s in finishTime.split(':'))
        start = start_hour * 60 + start_minute
        end = end_hour * 60 + end_minute

        if 0 <= end - start < 15:
            return 0  # Special case
        return end // 15 - (start + 14) // 15 + (start > end) * (24 * 4)


        # My method
        def get_time(time: str):
            hour, minute = time.split(':')
            return int(hour), int(minute)

        def adjust_time(time: str, mode: str):
            bins = [0, 15 ,30, 45, 60]

            hour, minute = get_time(time)

            new_min = minute
            if mode == 'start':
                for b in bins[-1::-1]:
                    if minute <= b:
                        new_min = b

            if mode == 'finish':
                for b in bins[:4]:
                    if minute >= b:
                        new_min = b

            return hour, new_min

        def first_larger(start, end):
            start_hour, start_minute = get_time(start)
            end_hour, end_minute = get_time(end)

            return start_hour * 60 + start_minute > end_hour * 60 + end_minute

        larger = True if first_larger(startTime, finishTime) else False

        start_hour, start_minute = adjust_time(startTime, mode='start')
        end_hour, end_minute = adjust_time(finishTime, mode='finish')

        diff = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
        if larger:
            diff += 24 * 60

        return max(diff // 15, 0)
