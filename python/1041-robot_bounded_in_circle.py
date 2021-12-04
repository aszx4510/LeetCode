
# 1041. Robot Bounded In Circle

# https://leetcode.com/problems/robot-bounded-in-circle/
# https://leetcode.com/problems/robot-bounded-in-circle/solution/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # North, East, West and South
        idx = 0
        x = y = 0

        for i in instructions:
            if i == 'R':
                idx = (idx + 1) % 4
            elif i == 'L':
                idx = (idx + 3) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        return (x == 0 and y == 0) or idx != 0
