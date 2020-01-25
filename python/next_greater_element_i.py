
# 496. Next Greater Element I

# https://leetcode.com/problems/next-greater-element-i/


class Solution(object):
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}
        for num in nums2:
            while stack and num > stack[-1]:
                ans[stack.pop()] = num
            stack.append(num)

        result = [ans.get(num, -1) for num in nums1]
        return result
