from typing import overload


@overload
def process(response: None) -> None:
    ...


@overload
def process(response: int) -> tuple[int, str]:
    ...


@overload
def process(response: bytes) -> str:
    ...


def process(response: int | bytes | None) -> str | None | tuple[int, str]:
    ...



"""
TODO:

foo is a function that returns an integer when second argument is 1, returns a string when second argument is 2, returns a list when second argument is 3, otherwise it returns the first argument.
"""


from typing import Any, Literal, overload, TypeVar

# Before 3.12 you have to write:
# T = TypeVar('T')
#
# def foo(value: T, flag: Any) -> T:


@overload
def foo(value: Any, flag: Literal[1]) -> int:
    ...


@overload
def foo(value: Any, flag: Literal[2]) -> str:
    ...


@overload
def foo(value: Any, flag: Literal[3]) -> list[Any]:
    ...


@overload
def foo[T](value: T, flag: Any) -> T:
    ...


def foo(value: Any, flag: Any) -> Any:
    ...
