
# 739. Daily Temperatures

# https://leetcode.com/problems/daily-temperatures/
# https://leetcode.com/problems/daily-temperatures/discuss/109832/Java-Easy-AC-Solution-with-Stack


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # Concise version
        stack = []
        result = [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < T[i]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append(i)
        return result


        # My version
        stack = []
        result = [0] * len(T)
        for i, t in enumerate(T):
            if not stack or stack[-1][1] >= t:
                stack.append((i, t))
            else:
                while stack and stack[-1][1] < t:
                    prev_i, prev_t = stack.pop()
                    result[prev_i] = i - prev_i
                stack.append((i, t))
        return result
