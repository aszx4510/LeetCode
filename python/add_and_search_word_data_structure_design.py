
# 211. Add and Search Word - Data structure design

# https://leetcode.com/problems/add-and-search-word-data-structure-design/


class TrieNode():
    """docstring for TrieNode"""
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


# Reference to #208
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, trie_node):
            # print(word)
            for i in range(len(word)):
                if word[i] == '.':
                    for child in trie_node.children.values():
                        found = helper(word[i+1:], child)
                        if found:
                            return True
                    return False
                else:
                    trie_node = trie_node.children.get(word[i])
                    if trie_node is None:
                        return False
            return trie_node.is_word

        return helper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
