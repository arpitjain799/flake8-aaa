from typing import NamedTuple


class Flake8Error(NamedTuple):
    line_number: int
    offset: int
    text: str
    checker_cls: type


class AAAError(NamedTuple):
    line_number: int
    offset: int
    text: str
