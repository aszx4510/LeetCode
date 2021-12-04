
# 1032. Stream of Characters

# https://leetcode.com/problems/stream-of-characters/
# https://leetcode.com/problems/stream-of-characters/discuss/278250/Python-Trie-Solution-with-Explanation
# https://leetcode.com/problems/stream-of-characters/discuss/278250/Python-Trie-Solution-with-Explanation/265423


class StreamChecker:
    # According to the Hint 1: Put the words into a trie, and manage a set of pointers within that trie.
    # Simple version, run time: 6348 ms
    def __init__(self, words: List[str]):
        self.wait_list = []
        self.trie = dict()

        for w in words:
            temp_dict = self.trie
            for c in w:
                temp_dict = temp_dict.setdefault(c, dict())
            temp_dict['#'] = '#'

    def query(self, letter: str) -> bool:
        new_wait = []
        if letter in self.trie:
            new_wait.append(self.trie[letter])
        for item in self.wait_list:
            if letter in item:
                new_wait.append(item[letter])

        self.wait_list = new_wait
        return any('#' in wait for wait in self.wait_list)


    # Concise version, run time: 604 ms
    def __init__(self, words: List[str]):
        T = lambda: collections.defaultdict(T)
        self.trie = T()

        for w in words:
            reduce(dict.__getitem__, w[::-1], self.trie)['#'] = '#'
        self.S = ''
        self.W = max(map(len, words))

    def query(self, letter: str) -> bool:
        self.S = (letter + self.S)[:self.W]
        curr = self.trie
        for c in self.S:
            if c in curr:
                curr = curr[c]
                if curr['#'] == '#':
                    return True
            else:
                break
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
