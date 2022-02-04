
# 454. 4Sum II

# https://leetcode.com/problems/4sum-ii/
# https://leetcode.com/problems/4sum-ii/solution/
# https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Concise version
        AB = Counter(a+b for a in nums1 for b in nums2)
        return sum(AB[-c-d] for c in nums3 for d in nums4)


        # Hashmap
        ans, m = 0, {}
        for a in nums1:
            for b in nums2:
                m[a + b] = m.get(a + b, 0) + 1
        for c in nums3:
            for d in nums4:
                ans += m.get(-(c + d), 0)
        return ans
