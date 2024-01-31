class Solution:
    def isPalindrome(self, s: str) -> bool:
        _list = list(s)
        _size = len(_list)
        left, right = 0, _size - 1

        while left <= right:
            while not _list[left].isalnum() and left < right:
                left += 1
            while not _list[right].isalnum() and right > left:
                right -= 1

            if _list[left].lower() != _list[right].lower():
                return False
            right -= 1
            left += 1

        return True

# 优化后

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:  # Check for empty string
            return True

        left, right = 0, len(s) - 1

        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1

            while right > left and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
