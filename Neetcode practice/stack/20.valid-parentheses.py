class Solution:
    def getReverseSymbol(self, origin:str) -> str:
        if origin==')':
            return '('
        elif origin=='}':
            return '{'
        else:
             return '['

    def isValid(self, s: str) -> bool:
        _stack=[]
        for item in list(s):
            if item=="(" or item=="{" or item=="[":
                _stack.append(item)
            if item==")" or item=="}" or item=="]":
                if len(_stack)==0:
                    return False
                if _stack[len(_stack)-1]==self.getReverseSymbol(item):
                    del _stack[len(_stack)-1]
                if _stack[len(_stack)-1]!=self.getReverseSymbol(item):
                    return False
        if len(_stack)==0:
            return True
        return False

ss=Solution()
# print(ss.isValid("()[({[})]{}"))
print(ss.isValid("(])"))


# 优化后
class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {')': '(',
                     '}': '{',
                     ']': '['
                  }
        open_chars = set(['(', '{', '['])

        _stack = []
        for char in s:
            if char in open_chars:
                _stack.append(char)
            elif char in pair_map:
                if not _stack or _stack[-1] != pair_map[char]: # not _stack会自动判断长度
                    return False
                _stack.pop()

        return len(_stack) == 0
