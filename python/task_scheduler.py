
# 621. Task Scheduler

# https://leetcode.com/problems/task-scheduler/
# https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_count = max(counter.values())
        max_members = list(counter.values()).count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_members)
