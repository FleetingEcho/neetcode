```python
判断为假的常见值
数值0（包括整数和浮点数）
空字符串""
空列表[]
空元组()
空字典{}
空集合set()
特殊对象None




a_num=ord('a')  返回97 ，
a_char=chr(a_num)

testStr = ''.join(char_list)  转换成string

world_str='world_str'
greeting = f"Hello, {world_str}"

```

f-string的用法:

>在Python中，f-string（格式化字符串字面量）是一种非常灵活且强大的字符串格式化机制。它允许您在字符串内直接嵌入Python表达式，并通过大括号 {} 进行标记。这些表达式在运行时被求值并格式化为字符串。f-string不仅可以用于插入变量，还能用于执行各种操作和表达式。以下是一些f-string的高级用法：


```python

表达式计算：
a = 5
b = 10
result = f"Five plus ten is {a + b}"  # "Five plus ten is 15"


调用函数和方法：
name = "world"
result = f"Hello, {name.upper()}"  # "Hello, WORLD"

格式化数字：
number = 123.4567
formatted = f"Formatted number: {number:.2f}"  # "Formatted number: 123.46"

使用字典和列表：
data = {'key': 'value'}
result = f"The value is {data['key']}"  # "The value is value"

list_items = [1, 2, 3]
result = f"The first item is {list_items[0]}"  # "The first item is 1"


条件表达式（三元操作符）：
condition = True
result = f"Condition is {'true' if condition else 'false'}"  # "Condition is true"


花括号转义：
如果您需要在f-string中包含花括号，可以通过双写花括号来转义它们：
result = f"{{this is in curly braces}}"  # "{this is in curly braces}"

内联操作和循环：
names = ['Alice', 'Bob', 'Charlie']
result = f"Names: {', '.join(name for name in names)}"  # "Names: Alice, Bob, Charlie"

```