
# 232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
# https://leetcode.com/problems/implement-queue-using-stacks/discuss/64198/Share-my-python-solution-(32ms)/179427


class MyQueue:

    # Concsie version
    # Approach 2: push O(1), pop amortized O(1)
    def __init__(self):
        self.s1, self.s2 = [], []


    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # We should check empty stack here
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # We should check empty stack here
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2


    # # My Version
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.s1, self.s2 = [], []
        

    # def push(self, x: int) -> None:
    #     """
    #     Push element x to the back of queue.
    #     """
    #     self.s1.append(x)
        

    # def pop(self) -> int:
    #     """
    #     Removes the element from in front of queue and returns that element.
    #     """
    #     # We should check empty stack here
    #     while len(self.s1) > 0:
    #         self.s2.append(self.s1.pop())
    #     pop_value = self.s2.pop()
    #     while len(self.s2) > 0:
    #         self.s1.append(self.s2.pop())
    #     return pop_value

    # def peek(self) -> int:
    #     """
    #     Get the front element.
    #     """
    #     # We should check empty stack here
    #     while len(self.s1) > 0:
    #         self.s2.append(self.s1.pop())
    #     peek_value = self.s2[-1]
    #     while len(self.s2) > 0:
    #         self.s1.append(self.s2.pop())
    #     return peek_value
        

    # def empty(self) -> bool:
    #     """
    #     Returns whether the queue is empty.
    #     """
    #     return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
