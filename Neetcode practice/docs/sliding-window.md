```python
float('inf')   无限大
-float('inf')   无限小


没有表示法来表示整数的无限大和无限小
当涉及到实际的整数界限时，通常会使用该数据类型所能表示的最大或最小值，例如 sys.maxsize 和 -sys.maxsize - 1 在Python中分别用于表示最大和最小的整数。



滑动窗口模板：
def sliding_window(s, t):
    window = {}
    need = {}
    # 将要匹配的 target 写入 need 中
    for c in t:
        need[c] = need.get(c, 0) + 1

    left, right = 0, 0
    valid = 0

    while right < len(s):
        # 右移窗口
        c = s[right]
        right += 1
        # 进行窗口内数据的一系列更新
        #
        # 例如 window 中有需要的值，并且个数相同，则 valid++
        # 例如 window[c] = window.get(c, 0) + 1

        # debug 输出的位置
        print("window: [%d, %d)" % (left, right))
        # ...

        # 判断左侧窗口是否要收缩
        while 'window needs shrink':
            # ... 进行一系列操作
            d = s[left]
            # 左移窗口
            left += 1
            # 进行窗口内数据的一系列更新
            if need.get(d):
                if window.get(d) == need[d]:
                    valid -= 1
                window[d] = window.get(d, 0) - 1

    return valid

# 示例调用
print(sliding_window("some string", "target"))

 * 滑动窗口题目:
 *
 * 3. 无重复字符的最长子串
 *
 * 30. 串联所有单词的子串
 *
 * 76. 最小覆盖子串
 *
 * 159. 至多包含两个不同字符的最长子串
 *
 * 209. 长度最小的子数组
 *
 * 239. 滑动窗口最大值
 *
 * 567. 字符串的排列
 *
 * 632. 最小区间
 *
 * 727. 最小窗口子序列
 *

```