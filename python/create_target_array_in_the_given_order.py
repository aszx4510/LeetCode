
# 1389. Create Target Array in the Given Order

# https://leetcode.com/problems/create-target-array-in-the-given-order/
# https://leetcode.com/problems/create-target-array-in-the-given-order/discuss/549583/O(nlogn)-based-on-%22smaller-elements-after-self%22.
# https://leetcode.com/problems/create-target-array-in-the-given-order/discuss/553334/Python-Using-insert()-and-without-insert()


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, ind in enumerate(index):
            if ind == len(result):
                result.append(nums[i])
            else:
                result = result[:ind] + [nums[i]] + result[ind:]
        return result
