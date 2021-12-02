
# 189. Rotate Array

# https://leetcode.com/problems/rotate-array/description/
# https://discuss.leetcode.com/topic/14341/easy-to-read-java-solution
# https://leetcode.com/problems/rotate-array/solution/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Cyclic replacement
        n = len(nums)
        k = k % n

        start = cnt = 0
        while cnt < n:
            current = start
            prev_val = nums[current]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev_val = prev_val, nums[next_idx]

                current = next_idx
                cnt += 1

                if start == current:
                    break
            start += 1
        return


        # Reverse method with two pointer
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k = k % n

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return
