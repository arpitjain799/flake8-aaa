from error_codes import AAAError, Flake8Error


class Flake8AAAException(Exception):
    pass


class TokensNotLoaded(Flake8AAAException):
    """
    `Checker.all_funcs()` was called before `ast_tokens` was populated. Usually
    this is done by `Checker.load()`.
    """


class EmptyBlock(Flake8AAAException):
    """
    Block has no nodes.
    """


class ValidationError(Flake8AAAException):

    def __init__(self, line_number: int, offset: int, text: str) -> None:
        self.line_number = line_number
        self.offset = offset
        self.text = text

    def to_flake8(self, checker_cls: type) -> Flake8Error:
        """
        Args:
            checker_cls: Class performing the check to be passed back to flake8.
        """
        return Flake8Error(
            line_number=self.line_number,
            offset=self.offset,
            text=self.text,
            checker_cls=checker_cls,
        )

    def to_aaa(self) -> AAAError:
        return AAAError(
            line_number=self.line_number,
            offset=self.offset,
            text=self.text,
        )
