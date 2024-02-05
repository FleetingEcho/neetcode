class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_range(nums, start, end):
            max_if_robbed_last = 0
            max_if_not_robbed_last = 0

            for i in range(start, end + 1):
                current_max_if_robbed = max_if_not_robbed_last + nums[i]
                current_max_if_not_robbed = max(max_if_robbed_last, max_if_not_robbed_last)

                #renew value
                max_if_not_robbed_last = current_max_if_not_robbed
                max_if_robbed_last = current_max_if_robbed

            return max(max_if_robbed_last, max_if_not_robbed_last)

        return max(rob_range(nums, 0, n - 2), rob_range(nums, 1, n - 1))
