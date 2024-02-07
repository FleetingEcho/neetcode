from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stack = []
        carry = 1

        for digit in reversed(digits):
            stack.append((digit + carry) % 10)
            carry = (digit + carry) // 10
        if carry:
            stack.append(carry)
        return list(reversed(stack))
