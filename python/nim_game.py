
# 292. Nim Game

# https://leetcode.com/problems/nim-game/
# http://forum.tfcis.org/forum.php?mod=viewthread&tid=386
# https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/494429/
# https://zhuanlan.zhihu.com/p/52931007


class Solution:
    def canWinNim(self, n: int) -> bool:
        if not n or n % 4 == 0:
            return False
        return True
