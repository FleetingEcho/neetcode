# 括号生成
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [("", 0, 0)]
        while stack:
            s, left, right = stack.pop()
            if left == n and right == n:
                res.append(s)
            if left < n:
                stack.append((s + '(', left + 1, right))
            if right < left:
                stack.append((s + ')', left, right + 1))
        return res
