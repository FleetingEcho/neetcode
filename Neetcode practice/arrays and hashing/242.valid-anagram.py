class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_map={}
        t_map={}
        for item in s:
            s_map[item]=s_map.get(item,0)+1
        for item in t:
            t_map[item]=t_map.get(item,0)+1
        for item in s_map.keys():
            if s_map[item]!=t_map.get(item,0):
                return False
        return True

# 优化后  single map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        for char in t:
            if char not in char_map:
                return False
            char_map[char] -= 1
            if char_map[char] < 0:
                return False

        return True

