
# 716. Max Stack

# https://leetcode.com/problems/max-stack/


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # (value, max_value)

    def push(self, x: int) -> None:
        self.stack.append((x, max(self.peekMax(), x)))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return ~sys.maxsize

    def popMax(self) -> int:
        max_value = self.peekMax()
        temp_stack = []
        while self.top() != max_value:
            temp_stack.append(self.pop())
        self.pop()
        while temp_stack:
            self.push(temp_stack.pop())
        return max_value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
