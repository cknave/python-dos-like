from typing import Any, Callable
from _typeshed import ReadableBuffer, WriteableBuffer


class CData:
    ...

    def __getitem__(self, item: int) -> Any:
        ...

    def __add__(self, other: int) -> CData:
        ...


class buffer:

    def __init__(self, cdata: CData, size: int = ...):
        ...


class FFI:
    NULL: CData

    def cdef(self,
             csource: str,
             override: bool = ...,
             packed: bool = ...,
             pack: int | None = ...) -> None:
        ...

    def compile(self,
                tmpdir: str = ...,
                verbose: int = ...,
                debug: bool | None = ...):
        ...

    def def_extern(self) -> Callable[..., Any]:
        ...

    def from_buffer(
        self,
        cdecl: str | ReadableBuffer | WriteableBuffer | buffer,
        python_buffer: ReadableBuffer | WriteableBuffer | buffer = ...,
        require_writable: bool = ...,
    ):
        ...

    def new(self, cdecl: str, init: Any = ...):
        ...

    def set_source(self,
                   module_name: str,
                   source: str,
                   source_extension: str = ...,
                   **kwds) -> None:
        ...

    def set_source_pkgconfig(self,
                             module_name: str,
                             pkgconfig_libs: list[str],
                             source: str,
                             source_extension: str = ...,
                             **kwds) -> None:
        ...

    def string(self, cdata: CData, maxlen: int = ...):
        ...
