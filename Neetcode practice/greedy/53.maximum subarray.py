from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_seen = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_seen = max(max_seen, max_current)
        return max_seen
