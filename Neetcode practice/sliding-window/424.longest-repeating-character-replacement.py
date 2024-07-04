def characterReplacement(s: str, k: int) -> int:
    window = dict()
    left = 0
    right = 0
    max_char_freq = 0
    max_length = 0

    while right < len(s):
        c = s[right]
        window[c] = window.get(c, 0) + 1
        max_char_freq = max(max_char_freq, window[c])
        right += 1

        # 判断是否需要收缩窗口
        while (right - left) - max_char_freq > k:
            d = s[left]
            window[d] -= 1
            if window[d] == 0:
                del window[d]
            left += 1
            # 更新最大字符频率，因为左边界移动，可能影响频率
            max_char_freq = max(window.values(), default=0)

        # 更新最大长度
        max_length = max(max_length, right - left)

    return max_length

# 测试
print(characterReplacement("AABABBA", 1))  # 输出 4
