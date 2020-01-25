
# 503. Next Greater Element II

# https://leetcode.com/problems/next-greater-element-ii/
# https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice
# https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC++Python-Loop-Twice/102626


class Solution(object):
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Speedup version
        stack, ans = [], [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        # Second loop
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            if not stack:
                break
        return ans



        # Concise version
        stack, ans = [], [-1] * len(nums)
        for i in list(range(len(nums))) * 2:
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans


        # My version
        n = len(nums)
        nums = nums + nums
        stack = []
        ans = [-1] * n * 2
        max_num = float('-inf')
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                prev_i = stack.pop()
                ans[prev_i] = num
            stack.append(i)
        return ans[:n]
