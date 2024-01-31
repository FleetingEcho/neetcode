class Solution:
    def search(self, nums, target):
        return self.left_bound(nums, target)

    def left_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                #这是查找左边界
                right = mid - 1
                # 如果查找右边界，则： left=mid+1
                # 查找中间值 return mid

        #这是查找左边界
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
        #如果查找右边界，则
        # if right <0 or nums[right]!=target:
        #     return -1
        # return right

        #如果查找中间值，这里可以直接返回-1了
        # return -1
# O(logN)




