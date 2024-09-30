
# =================
# 泛型函数
from typing import TypeVar, Tuple

T = TypeVar('T')

def swap(a: T, b: T) -> Tuple[T, T]:
    return b, a

# 使用泛型函数
x, y = swap(1, 2)             # 处理整数
print(x, y)  # 输出: 2 1

x, y = swap("hello", "world")  # 处理字符串
print(x, y)  # 输出: world hello



# 泛型类

from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

    def get_content(self) -> T:
        return self.content

# 使用泛型类 Box
int_box = Box(123)           # Box[int]
print(int_box.get_content())  # 输出: 123

str_box = Box("hello")       # Box[str]
print(str_box.get_content())  # 输出: hello


#泛型与多个变量

from typing import TypeVar, Tuple

T = TypeVar('T')
U = TypeVar('U')

def pair(a: T, b: U) -> Tuple[T, U]:
    return a, b

# 使用泛型函数处理不同类型的输入
p1 = pair(1, "apple")       # Tuple[int, str]
print(p1)  # 输出: (1, 'apple')

p2 = pair(True, 3.14)       # Tuple[bool, float]
print(p2)  # 输出: (True, 3.14)


# 泛型与约束


from typing import TypeVar

class Comparable:
    def __lt__(self, other):
        return NotImplemented

T = TypeVar('T', bound=Comparable)

def compare(a: T, b: T) -> bool:
    return a < b

# 假设有一个类继承自 Comparable
class Number(Comparable):
    def __init__(self, value: int):
        self.value = value

    def __lt__(self, other: 'Number') -> bool:
        return self.value < other.value

# 使用受限的泛型函数
n1 = Number(5)
n2 = Number(10)

print(compare(n1, n2))  # 输出: True



# 泛型方法

from typing import Generic, TypeVar,Callable

T = TypeVar('T')
U = TypeVar('U')

class Container(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

    def update(self, new_content: T) -> None:
        self.content = new_content

    def transform(self, func: Callable[[T], U]) -> U:
        return func(self.content)

# 使用泛型类
container = Container(10)

# 使用泛型方法 `update`
container.update(20)
print(container.content)  # 输出: 20

# 使用泛型方法 `transform`
def to_string(x: int) -> str:
    return f"Number: {x}"

result = container.transform(to_string)
print(result)  # 输出: Number: 20




# 泛型别名

from typing import List, Tuple, TypeVar

T = TypeVar('T')
PairList = List[Tuple[T, T]]  # 泛型别名

def process_pairs(pairs: PairList[int]) -> None:
    for a, b in pairs:
        print(f"Pair: {a}, {b}")

# 使用泛型别名
pairs = [(1, 2), (3, 4), (5, 6)]
process_pairs(pairs)


# 泛型迭代器

from typing import Iterator, TypeVar

T = TypeVar('T')

def my_iterable(items: Iterator[T]) -> None:
    for item in items:
        print(item)

# 使用泛型迭代器函数
my_iterable(iter([1, 2, 3]))  # 迭代整数
my_iterable(iter(["a", "b", "c"]))  # 迭代字符串


# 限制类型


from typing import TypeVar

# 限制 T 为 int 或 str 的子类
T = TypeVar('T', bound=int | str)
# 限制 T 只能是 int 或 str，并且两个参数必须具有相同类型
T = TypeVar('T', int, str)
# 限制 T 为 int 或其子类
T = TypeVar('T', bound=int)

def add(a: T, b: T) -> T:
    return a + b

# 示例调用
result_int = add(1, 2)          # 正确，整数类型
result_str = add("hello", " world")  # 正确，字符串类型
# result_invalid = add(1, "two")  # expect-type-error，类型不匹配






from typing import TypeVar, Type

# 定义一个泛型变量 T，表示任意类型
T = TypeVar('T')

# 使用 Type 来指定参数是一个类，并且返回该类的实例
def make_object(cls: Type[T]) -> T:
    return cls()


# 扩展字段

from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str


# 定义 Undergraduate 类，继承 Student 并添加 major 字段
class Undergraduate(Student):
    major: str  # 新增的字段，表示专业

    ...



from typing import Any
from typing import TypeGuard


def is_string(value: Any) -> TypeGuard[str]:
    return isinstance(value, str)

