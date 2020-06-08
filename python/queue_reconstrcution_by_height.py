
# 406. Queue Reconstruction by Height

# https://leetcode.com/problems/queue-reconstruction-by-height/
# https://leetcode.com/problems/queue-reconstruction-by-height/solution/
# https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
