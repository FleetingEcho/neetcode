# 必须要大写的类型
from typing import Any, Iterable, Union,Optional,Tuple,Callable,Type,Literal,Final,TypedDict, NamedTuple,Protocol, cast
def foo(args:Any):
    ...

def foo1(x: dict[str, str]) -> None:
    ...


my_list:Final = []  # cannot change , like const in js


def both_example(*args: int | str, **kwargs: int) -> None:
    print("args:", args)
    # args: (1, 2, 3)
    print("kwargs:", kwargs)
    # kwargs: {'a': 4, 'b': 5}

both_example(1, 2, 3, a=4, b=5)

def foo3(x: list[str | int | float | list]) -> None:
    ...

from typing import Protocol

class Shape(Protocol):
    name:str
    @property
    def area(self) -> float:
        ...

    @property
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float) -> None:
        ...

class Rectangle(Shape):  # 显式继承 Shape 协议
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @property
    def area(self) -> float:
        return self._width * self._height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

# 创建对象并访问属性
rect = Rectangle(3, 4)
print(rect.area)  # 输出: 12

# 修改属性，触发 setter
rect.width = 5
print(rect.area)  # 输出: 20

# 直接访问属性触发 getter
print(rect.width)  # 输出: 5



def foo(x: int | None = None) -> None:
    pass

# 正确调用
foo()         # 没有参数
foo(5)        # 整数参数
foo(None)     # None

def foo(x:Tuple[str,int]):
    pass

foo(('1',1))

# 声明 type
Vector = list[float]



# 类型转换
a: Any = 42  # 定义为 Any 类型

# 使用 cast 将 a 显式转换为 int 类型
a = cast(int, a)


from typing import Callable

# 定义一个函数类型
FuncType = Callable[[int, int], int]

# 使用标准函数定义，并在函数签名中使用类型别名
def subtract(a: int, b: int) -> int:
    return a - b

# 另一种简洁的方法是使用 lambda 表达式
subtract_lambda: FuncType = lambda a, b: a - b

# 使用函数
print(subtract(5, 3))          # 输出: 2
print(subtract_lambda(5, 3))   # 输出: 2

def unknown_function(*args) -> int:
    return 42

# 使用 cast 显式声明这个函数为 FuncType 类型
typed_func = cast(FuncType, unknown_function)




# ===============

from typing import Awaitable

def run_async(x: Awaitable[int]) -> None:
    async def execute():
        result = await x
        print(f"Result: {result}")

    # 执行异步任务
    import asyncio
    asyncio.run(execute())

# 示例：创建一个返回整数的异步函数
async def async_function() -> int:
    return 42

# 调用 run_async，传入 awaitable int
run_async(async_function())



"""
TODO:

Define a callable type that accepts a string argument and returns None.
*The parameter name can be arbitrary.*
"""
from typing import Callable

SingleStringInput = Callable[[str], None]



from typing import ClassVar

class Foo:
    # 类变量，类型注解为 int
    bar: ClassVar[int] = 0
    # bar: ClassVar[int]：ClassVar 是 typing 模块中的一个类型注解，表示 bar 是一个类变量，并且它的类型应该是 int。


from typing import Callable, TypeVar

# 定义一个泛型，适用于任何函数签名
F = TypeVar('F', bound=Callable[..., None])

def decorator(func: F) -> F:
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper  # 类型 F 确保返回值与输入函数类型一致

# 示例函数
@decorator
def say_hello(name: str) -> None:
    print(f"Hello, {name}!")

# 使用装饰器调用
say_hello("World")
# Before calling say_hello
# Hello, World!
# After calling say_hello


# 指定字面量

from typing import Literal

def foo(direction: Literal['left', 'right']) -> None:
    pass

def foo(direction: Literal['left'] | Literal['right']) -> None:
    pass



def execute_query(sql: str, parameters: Iterable[Any]) -> None:
    # 例如：sqlite3、psycopg2 等数据库驱动支持参数化查询
    print(f"Executing query: {sql} with parameters: {parameters}")

# 调用示例
execute_query("SELECT * FROM users WHERE id = ?", (123,))  # 传递元组 (int)
execute_query("SELECT * FROM users WHERE username = ?", ["john_doe"])  # 传递列表 (str)


from typing import Self

class Foo:
    def return_self(self) -> Self:
        return self  # 返回当前实例
