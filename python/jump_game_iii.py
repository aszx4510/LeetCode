
# 1306. Jump Game III

# https://leetcode.com/problems/jump-game-iii/


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue, arrived = [start], set([start])
        while queue:
            now = queue.pop(0)
            if arr[now] == 0:
                return True

            left = now - arr[now] if now - arr[now] >= 0 else None
            right = now + arr[now] if now + arr[now] < len(arr) else None

            if left is not None and left not in arrived:
                queue.append(left)
                arrived.add(left)

            if right is not None and right not in arrived:
                queue.append(right)
                arrived.add(right)
        return False
