```python

不可哈希对象的例子：
**列表（list）和字典（dict）**是不可哈希的，因为它们是可变的，它们的内容可以改变，所以没有固定的哈希值。

collections.Counter 是 Python 中一个非常有用的数据结构，它是字典的一个子类，用于计数可哈希对象。它主要用于计算各个元素在某个集合中出现的次数。Counter 可以用于字符串、列表、元组等可迭代对象。


from collections import Counter
基本使用
计数元素


# 使用列表
cnt = Counter(['a', 'b', 'c', 'a', 'b', 'b', 'a', 'c'])
print(cnt)  # 输出: Counter({'a': 3, 'b': 3, 'c': 2})

# 使用字符串
cnt = Counter("abracadabra")
print(cnt)  # 输出: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
获取最常见的元素


cnt = Counter('abracadabra')
print(cnt.most_common(3))  # 输出 [('a', 5), ('b', 2), ('r', 2)]
更新计数


cnt = Counter()
cnt.update("abcdaab")
print(cnt)  # 输出: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

cnt.update({'a':1, 'd':5})
print(cnt)  # 输出: Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
其他操作
元素的计数：cnt['a'] 会返回 'a' 出现的次数。
总数：sum(cnt.values()) 会返回所有计数的总和。
组合和差分：Counter 支持加法和减法操作。
示例


c1 = Counter(a=4, b=2, c=0, d=-2)
c2 = Counter(['a', 'b', 'b', 'c'])

# 组合
c1 + c2  # Counter({'a': 5, 'b': 4, 'c': 1, 'd': -2})

# 差分
c1 - c2  # Counter({'a': 3, 'd': -2})
```