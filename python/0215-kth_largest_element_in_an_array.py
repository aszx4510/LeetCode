
# 215. Kth Largest Element in an Array

# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60294/Solution-explained


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def findKthSmallest(nums, k):
            if nums:
                pos = partition(nums, 0, len(nums) - 1)
                if k > pos + 1:
                    return findKthSmallest(nums[pos+1:], k - pos - 1)
                elif k < pos + 1:
                    return findKthSmallest(nums[:pos], k)
                else:
                    return nums[pos]

        def partition(nums, left, right):
            # choose the right-most element as pivot
            low = left
            while left < right:
                if nums[left] < nums[right]:
                    nums[left], nums[low] = nums[low], nums[left]
                    low += 1
                left += 1
            nums[low], nums[right] = nums[right], nums[low]
            return low

        # Quick selection
        return findKthSmallest(nums, len(nums) - k + 1)


        # Another method, much faster than quick selection
        return heapq.nlargest(k, nums)[k - 1]
