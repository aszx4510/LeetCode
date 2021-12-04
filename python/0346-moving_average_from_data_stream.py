
# 346. Moving Average from Data Stream

# https://leetcode.com/problems/moving-average-from-data-stream/


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.cnt = 0
        self.nums = []
        self.num_sum = 0

    def next(self, val: int) -> float:
        self.num_sum += val
        self.nums.append(val)
        self.cnt += 1
        
        if self.cnt > self.size:
            self.num_sum -= self.nums.pop(0)
            self.cnt -= 1

        return self.num_sum / self.cnt


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
