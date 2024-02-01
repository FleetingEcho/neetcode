from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map={}
        for index, val in enumerate(nums):
            need=target - val
            if _map.get(need)!= None:
                return [index,_map.get(need)]
            _map[val]=index


# 优化后
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        for index, val in enumerate(nums):
            need = target - val
            if need in _map:
                return [_map[need], index]
            _map[val] = index
