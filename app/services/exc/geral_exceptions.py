class InvalidInput(Exception):
    cursor: any
    diag: any
    pgcode: any
    pgerror: any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __setstate__(self, state): ...
class IncorrectField(Exception):
    cursor: any
    diag: any
    pgcode: any
    pgerror: any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __setstate__(self, state): ...
class InvalidId(Exception):
    cursor: any
    diag: any
    pgcode: any
    pgerror: any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __setstate__(self, state): ...
class MissingField(Exception):
    cursor: any
    diag: any
    pgcode: any
    pgerror: any
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __setstate__(self, state): ...

    ## :this-is-fine: