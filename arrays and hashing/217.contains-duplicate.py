from type import List
class Solution:
      def containsDuplicate(self, nums: List[int]) -> bool:
          numset={}
          for i in nums:
              if i not in numset:
                  numset[i]=1
              else:
                  return True
          return False

# 优化后
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
