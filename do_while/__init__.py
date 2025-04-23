# Copyright Amethyst Reese
# Licensed under the MIT license

"""
making poor life choices for conference talks
"""

from .__version__ import __version__

__author__ = "Amethyst Reese"


from collections.abc import Callable, Collection
from typing import Any, TypeAlias

Loop: TypeAlias = Callable[[], None]
Predicate: TypeAlias = Callable[[], bool] | Collection[Any]


def _check(predicate: Predicate) -> bool:
    assert predicate not in (  # type:ignore
        True,
        False,
        None,
    ), f"predicate is {predicate}, must be callable or collection"

    if callable(predicate):
        return predicate()
    else:
        return bool(predicate)


class do:
    _wrapped: Loop = lambda: None
    _predicate: Predicate = lambda: False

    """
    Execute the decorated function at least once, until `predicate` is falsey.

    Does not execute until the `while_(...)` function is called.
    `predicate` must be a callable that returns a boolean value.

    Example:

        @do
        def loop():
            ... # do something

        while_(predicate)

    Equivalent of:

        while True:
            ... # do something

            if not predicate():
                break

    """

    def __init__(self, fn: Loop) -> None:
        def wrapped() -> None:
            while True:
                fn()
                if not _check(do._predicate):
                    break

        do._wrapped = wrapped


def while_(predicate: Predicate) -> None:
    """
    Execute the pending do-while loop.

    `predicate` must be a callable that returns a truthy value.
    """
    do._predicate = predicate
    do._wrapped()


def until(predicate: Predicate) -> Callable[[Loop], None]:
    """
    Execute the decorated function until `predicate` evaluates *truthy*.

    Inverse of a while loop.

    Example:

        @until(predicate)
        def loop():
            ... # body

    Equivalent of:

        while not predicate():
            ... # body

    """

    def wrapper(fn: Loop) -> None:
        def wrapped() -> None:
            while not _check(predicate):
                fn()

        wrapped()

    return wrapper
