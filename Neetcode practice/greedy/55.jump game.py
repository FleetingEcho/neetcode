class Solution:
  def can_jump(self,nums):
    farthest=0
    for i in range(nums):
      farthest=max(farthest,i+nums[i])
      if farthest<= i :
        return False
    return farthest>=len(nums)-1

#如果换成跳最少的次数，就是Jump2 的题目
