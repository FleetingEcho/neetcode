from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [n] * n

        def dp(nums, p):
            if p >= n - 1:
                return 0
            if memo[p] != n:
                return memo[p]
            steps = nums[p]
            for i in range(1, steps + 1):
                sub_problem = dp(nums, p + i)
                memo[p] = min(memo[p], sub_problem + 1)
            return memo[p]
        return dp(nums, 0)

#上面这种带有子问题的，基本都会超时，因为题目数组的长度是10**4.

#最好用greedy,通过一次遍历来确定每次跳跃可以到达的最远位置

class Solution:
    def jump(self, nums: List[int]) -> int:
            n = len(nums)
            end = 0
            farthest = 0
            jumps = 0
            for i in range(n - 1):
                farthest = max(nums[i] + i, farthest)
                if end == i: #跳到最远了，更新下一步的距离
                    jumps += 1
                    end = farthest
            return jumps

