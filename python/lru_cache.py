
# 146. LRU Cache

# https://leetcode.com/problems/lru-cache/
# https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList


class MyNode():
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = MyNode(0, 0)
        self.tail = MyNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        node = MyNode(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            temp_node = self.head.next
            self._remove(temp_node)
            del self.dic[temp_node.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
