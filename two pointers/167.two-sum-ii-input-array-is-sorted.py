from ast import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #已经是排序过的，不用再动
        return self.n_sum_target(numbers,2,0,target)
    def n_sum_target(self,nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        res = []
        # 至少是 2Sum，且数组大小不应该小于 n
        if n < 2 or sz < n:
            return res
        #2Sum 是 base case
        if n == 2:
            #双指针那一套操作
            lo, hi = start, sz - 1
            while lo < hi:
                sum_ = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if sum_ < target:
                    while lo < hi and nums[lo] == left: #跳重
                        lo += 1
                elif sum_ > target:
                    while lo < hi and nums[hi] == right: #跳重
                        hi -= 1
                else:
                    res.append(lo+1) #不同之处
                    res.append(hi+1)
                    while lo < hi and nums[lo] == left: #跳重
                        lo += 1
                    while lo < hi and nums[hi] == right: #跳重
                        hi -= 1
        else:
            i = start
            while i < sz: #不能用range,因为i无法控制，进行跳重
                sub = self.n_sum_target(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                i += 1 #自增
                while i < sz and nums[i] == nums[i - 1]:# 跳重，排好序了，跳过第一个数字重复的情况，否则会出现重复结果
                    i += 1
        return res