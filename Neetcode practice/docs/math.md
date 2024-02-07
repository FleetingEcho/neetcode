

```python
取模运算符 %：

功能：返回除法的余数。
示例：10 % 3 返回 1，因为 10 除以 3 的商为 3，余数为 1。
地板除法运算符 //：

功能：返回除法的整数部分，忽略小数部分，向下取整。
示例：10 // 3 返回 3，因为 10 除以 3 的结果是 3.333...，向下取整得到 3。
pow(x, y) 函数：

功能：返回 x 的 y 次方。
示例：pow(2, 3) 返回 8，因为 2 的 3 次方等于 8。
math.pow(x, y) 函数：

功能：返回 x 的 y 次方，与 pow() 函数功能相同，但是 math.pow() 是 math 模块提供的函数，需要导入模块后使用。
示例：math.pow(2, 3) 返回 8。
math.sqrt(x) 函数：

功能：返回 x 的平方根。
示例：math.sqrt(16) 返回 4，因为 4 的平方根是 2。
math.floor(x) 函数：

功能：返回不大于 x 的最大整数。
示例：math.floor(3.7) 返回 3。
math.ceil(x) 函数：

功能：返回不小于 x 的最小整数。
示例：math.ceil(3.2) 返回 4。
math.factorial(x) 函数：

功能：返回 x 的阶乘。
示例：math.factorial(5) 返回 120，因为 5 的阶乘是 5 * 4 * 3 * 2 * 1 = 120。
math.pi 常量：

功能：返回圆周率 π。
示例：math.pi 返回 3.141592653589793。
math.e 常量：

功能：返回自然对数的底数 e。
示例：math.e 返回 2.718281828459045。


quotient, remainder = divmod(10, 3)
print("Quotient:", quotient)   # 输出：Quotient商: 3
print("Remainder:", remainder) # 输出：Remainder余数: 1




Python 中没有一个函数可以判断一个字符串是否为合理的整数（包括正、负数）。str.isdigit() 可以判断正数，但是无法判断负数。
1.用try catch
2.用token[-1].isdigit():

python 的整数除法是向下取整，而不是向零取整。

python2 的除法 "/" 是整数除法， "-3 / 2 = -2";
python3 的地板除 "//" 是整数除法， "-3 // 2 = -2";
python3 的除法 "/" 是浮点除法， "-3 / 2 = -1.5";

办法:
int(num1 / float(num2))
无论如何，浮点数除法都会得到一个浮点数，比如 "-3 / 2.0 = 1.5" ；
此时再取整，就会得到整数部分，即 float(-1.5) = -1 。

可以用math.isnan()判断是不是非数字
```