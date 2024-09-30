
from typing import TypedDict

# 使用 TypedDict 定义具有特定键和值类型的字典
class Student(TypedDict):
    name: str   # 学生的姓名，类型为字符串
    age: int    # 学生的年龄，类型为整数
    school: str # 学生的学校名称，类型为字符串


from typing import TypedDict, NotRequired


# NotRequired：表示字段可以缺失。
# Optional[str]：表示字段可以存在，但值可以是 None 或 str。
class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]

from typing import TypedDict, NotRequired

class Person(TypedDict):
    name: str  # 必须字段
    age: NotRequired[int]  # 可选字段
    gender: NotRequired[str]  # 可选字段
    address: NotRequired[str]  # 可选字段
    email: NotRequired[str]  # 可选字段



# 解包

from typing import TypedDict, Unpack


class Person(TypedDict):
    name: str
    age: int


# 使用 Unpack 解包 TypedDict 到关键字参数
def foo(**kwargs: Unpack[Person]) -> None:
    name = kwargs["name"]
    age = kwargs["age"]
    print(f"Name: {name}, Age: {age}")
