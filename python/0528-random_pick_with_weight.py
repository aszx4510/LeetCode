
# 528. Random Pick with Weight

# https://leetcode.com/problems/random-pick-with-weight/
# https://leetcode.com/problems/random-pick-with-weight/discuss/154370/Please-someone-explain-this-question/249550
# https://leetcode.com/problems/random-pick-with-weight/discuss/154475/Python-1-liners-using-builtin-functions
# https://leetcode.com/problems/random-pick-with-weight/discuss/154475/Python-1-liners-using-builtin-functions/567371


class Solution:

    def __init__(self, w: List[int]):
        self.w = list(itertools.accumulate(w))
        

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))


# Another version, straight but low efficiency
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        

    def pickIndex(self) -> int:
        return random.choices(range(len(self.w)), weights=self.w)[0]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
