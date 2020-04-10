
# 155. Min Stack

# https://leetcode.com/problems/min-stack/
# https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution/49153


class MinStack:
    # Another method
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # (value, min_value)

    def push(self, x: int) -> None:
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return sys.maxsize


    # My version
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        min_value = min(self.min_stack[-1], x) if self.min_stack else x
        self.min_stack.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
