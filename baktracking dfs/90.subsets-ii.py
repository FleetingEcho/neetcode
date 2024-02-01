from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def backtrack(nums,start,track):
            temp_track=list(track)
            temp_track.sort()
            if temp_track not in res:
                res.append(temp_track)
            for index in range(start,len(nums)):
                track.append(nums[index])
                backtrack(nums,index+1,track)
                track.pop()

        track=[]
        backtrack(nums,0,track)
        return res


#优化后

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []

        def backtrack(start: int, track: List[int]) -> None:
            res.append(list(track))
            for index in range(start, len(nums)):
                # check duplicate
                if index > start and nums[index] == nums[index - 1]:
                    continue
                track.append(nums[index])
                backtrack(index + 1, track)
                track.pop()

        backtrack(0, [])
        return res
