from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def backtrack(start: int, track: List[int]) -> None:
            res.append(list(track))
            for index in range(start, len(nums)):
                track.append(nums[index])
                backtrack(index + 1, track)
                track.pop()

        backtrack(0, [])
        return res
