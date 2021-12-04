
# 212. Word Search II

# https://leetcode.com/problems/word-search-ii/
# https://leetcode.com/problems/word-search-ii/discuss/59780/Java-15ms-Easiest-Solution-(100.00)
# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i, j, path):
            if node.is_word:
                result.append(path)
                node.is_word = False
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            temp = board[i][j]
            node = node.children.get(temp)
            if not node:
                return
            board[i][j] = '#'
            dfs(node, i + 1, j, path + temp)
            dfs(node, i - 1, j, path + temp)
            dfs(node, i, j + 1, path + temp)
            dfs(node, i, j - 1, path + temp)
            board[i][j] = temp

        result = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(node, i, j, '')

        return result
