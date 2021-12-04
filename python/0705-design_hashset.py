
# 705. Design HashSet

# https://leetcode.com/problems/design-hashset/
# https://leetcode.com/problems/design-hashset/discuss/210494/Real-Python-Solution-no-cheating-open-addressing/415067


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 8
        self.size = 0
        self.arr = [None] * self.capacity
        self.thres = float(2) / 3

    # Can be modified to hash function
    def _hash(self, key):
        return key % self.capacity

    def _rehash(self, key):
        return (5 * key + 1) % self.capacity

    def _insert_pos(self, key):
        pos = self._hash(key)

        # use -1 to represent the 'removed' item
        while self.arr[pos] is not None:
            if self.arr[pos] == key:
                return -1
            # Here is the small bug, the following item may contain the key
            if self.arr[pos] == -1:
                break
            pos = self._rehash(pos)
        return pos

    def _safe_add(self, key):
        pos = self._insert_pos(key)

        # Already in the list
        if pos == -1:
            return

        self.arr[pos] = key
        self.size += 1

    def _safe_add_arr(self, arr):
        for val in arr:
            if val is not None:
                self._safe_add(val)

    def add(self, key: int) -> None:
        def pre_add(self):
            if self.size / self.capacity <= self.thres:
                return
            self.capacity <<= 1
            old_arr, self.arr = copy.deepcopy(self.arr), [None] * self.capacity
            self._safe_add_arr(old_arr)

        pre_add(self)

        # pre-check
        if self.contains(key):
            return
        self._safe_add(key)

    def remove(self, key: int) -> None:
        pos = self._hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key:
                self.arr[pos] = -1
                self.size -= 1
                return
            pos = self._rehash(pos)
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        pos = self._hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key:
                return True
            pos = self._rehash(pos)
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
