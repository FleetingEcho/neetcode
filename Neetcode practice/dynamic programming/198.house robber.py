from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        N = len(nums)
        dp = [0] * (N+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N+1):
            #k超前一位，第二家=max(抢0家和这家，或只抢上一家)
            dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])
        return dp[N]