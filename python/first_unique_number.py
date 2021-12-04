
# 1429. First Unique Number
# 30-Day LeetCoding Challenge: Week 4 Day 7

# https://leetcode.com/problems/first-unique-number/
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.seen, self.over_two = set(), set()
        self.position = dict()

        self.root, self.tail = ListNode(-1), ListNode(-1)
        self.root.next, self.tail.prev = self.tail, self.root

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.root.next.val if self.root.next else self.root.val

    def add(self, value: int) -> None:
        if value in self.over_two:
            pass
        elif value in self.seen:
            # Delete duplicate
            self._del(value)
            self.over_two.add(value)
        else:
            # Append to tail
            node = ListNode(value)
            tail_prev = self.tail.prev
            tail_prev.next, node.prev = node, tail_prev
            node.next, self.tail.prev = self.tail, node

            self.position[value] = node
            self.seen.add(value)

    def _del(self, value: int) -> None:
        node = self.position[value]
        prev_node, next_node = node.prev, node.next

        prev_node.next = next_node
        next_node.prev = prev_node


class DoubleListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
