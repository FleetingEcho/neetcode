from operator import add, mul, sub
from typing import List
import re

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": lambda x, y: add(x,y),
            "-": lambda x, y: sub(x,y),
            "*": lambda x, y: mul(x,y),
             "/": lambda x, y: int(x / float(y)),
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)

        return stack[0]

"""
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
"""


#或用正则


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": lambda x, y: add(x,y),
            "-": lambda x, y: sub(x,y),
            "*": lambda x, y: mul(x,y),
             "/": lambda x, y: int(x / float(y)),
        }

        stack = list()
        for token in tokens:
            if bool(re.match(r'^-?\d+$', token)): #包括正负数， 其他symbol被排除了
                num = int(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            stack.append(num)

        return stack[0]
