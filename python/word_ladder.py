
# 127. Word Ladder

# https://leetcode.com/problems/word-ladder/
# https://leetcode.com/problems/word-ladder/solution/


from collections import defaultdict
class Solution:
    # Approach 2: Bidirectional Breadth First Search with better efficiency
    def __init__(self):
        self.l = 0
        self.all_combo = defaultdict(list)

    def visit_word_node(self, queue, visited, other_visited):
        word, level = queue.pop(0)
        for i in range(self.l):
            intermediate_word = word[:i] + '*' + word[i + 1:]
            for possible_word in self.all_combo[intermediate_word]:
                if possible_word in other_visited:
                    return level + other_visited[possible_word]
                if possible_word not in visited:
                    visited[possible_word] = level + 1
                    queue.append((possible_word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        self.l = len(beginWord)
        for word in wordList:
            for i in range(self.l):
                self.all_combo[word[:i] + '*' + word[i + 1:]].append(word)

        begin_queue, end_queue = [(beginWord, 1)], [(endWord, 1)]
        begin_visited, end_visited = {beginWord: 1}, {endWord: 1}

        while begin_queue and end_queue:
            # 1 hop for begin word tree
            ans = self.visit_word_node(begin_queue, begin_visited, end_visited)
            if ans:
                return ans

            # 1 hop for end word tree
            ans = self.visit_word_node(end_queue, end_visited, begin_visited)
            if ans:
                return ans
        return 0


    # # Approach 1: Breadth First Search
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     if not beginWord or not endWord or not wordList or endWord not in wordList:
    #         return 0

    #     l = len(beginWord)
    #     all_combo = defaultdict(list)
    #     for word in wordList:
    #         for i in range(l):
    #             all_combo[word[:i] + '*' + word[i + 1:]].append(word)

    #     queue = [(beginWord, 1)]
    #     visited = {beginWord}
    #     while queue:
    #         word, level = queue.pop(0)
    #         for i in range(l):
    #             intermediate_word = word[:i] + '*' + word[i + 1:]
    #             for possible_word in all_combo[intermediate_word]:
    #                 if possible_word == endWord:
    #                     return level + 1
    #                 if possible_word not in visited:
    #                     visited.add(possible_word)
    #                     queue.append((possible_word, level + 1))
    #     return 0
