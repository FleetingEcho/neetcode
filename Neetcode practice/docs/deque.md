
deque是一个灵活且高效的容器类型，适用于需要频繁进行两端插入和删除操作的场景。O(1)

```python
常用操作：
创建：d = deque() 创建一个空的双端队列。

添加元素：
d.append(item)：在右端添加元素。
d.appendleft(item)：在左端添加元素。

移除元素：
d.pop()：移除并返回右端元素。
d.popleft()：移除并返回左端元素。

扩展：
d.extend(iterable)：使用可迭代对象在右端扩展队列。
d.extendleft(iterable)：使用可迭代对象在左端扩展队列（注意：左端扩展时，可迭代对象的顺序会被反转）。

旋转：
d.rotate(n)：右旋转n步（如果n是负数，则左旋转）。



from collections import deque

# 创建deque
d = deque()

# 添加元素
d.append(1)        # deque: [1]
d.appendleft(2)    # deque: [2, 1]

# 移除元素
d.pop()            # 返回 1, deque: [2]
d.popleft()        # 返回 2, deque: []

# 限制长度的deque
d = deque(maxlen=2)
d.append(1)        # deque: [1]
d.append(2)        # deque: [1, 2]
d.append(3)        # deque: [2, 3] （1 被挤出）

```