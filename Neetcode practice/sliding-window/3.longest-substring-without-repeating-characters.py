#无重复最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left, right = 0, 0
        max_length = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            # 当窗口内出现重复字符时，开始收缩左边界直到无重复
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            # 更新最大长度
            max_length = max(max_length, right - left)

        return max_length
