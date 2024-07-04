# 字符串排列
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 记录 s1 中各字符的频率
        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        left = 0
        right = 0

        while right < len(s2):
            # 更新窗口内数据
            s2_count[ord(s2[right]) - ord('a')] += 1
            right += 1

            # 判断左侧窗口是否需要收缩
            if right - left == len(s1):
                # 检查当前窗口是否匹配 s1 的字符频率
                if s2_count == s1_count:
                    return True

                # 将左侧字符移出窗口
                s2_count[ord(s2[left]) - ord('a')] -= 1
                left += 1

        return False

# 测试
sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))  # 输出 True
print(sol.checkInclusion("ab", "eidboaoo"))  # 输出 False
