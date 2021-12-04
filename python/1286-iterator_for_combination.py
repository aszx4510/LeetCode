
# 1286. Iterator for Combination

# https://leetcode.com/problems/iterator-for-combination/
# https://leetcode.com/problems/iterator-for-combination/discuss/451260/python-using-generator


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        def combinations(cur, idx):
            if len(cur) == combinationLength:
                yield ''.join(cur)
                return
            for i in range(idx, len(characters)):
                cur.append(characters[i])
                # yield from: https://www.python.org/dev/peps/pep-0380/#id11
                yield from combinations(cur, i + 1)
                cur.pop()

        self.combos = combinations([], 0)
        self.current = True
        self.has_next_called = False
        
    def next(self) -> str:
        if self.hasNext():
            self.has_next_called = False
            return self.current

    def hasNext(self) -> bool:
        if self.current and not self.has_next_called:
            self.has_next_called = True
            self.current = next(self.combos, False)
        return bool(self.current)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
