from __future__ import annotations

import threading
from typing import Callable, Optional

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

from . import _dos

MainFunc: TypeAlias = Callable[[], Optional[int]]
"""dos-like python main function."""

_bg_thread: BackgroundThread | None = None
_main_fn: MainFunc | None = None
_raised_exception: Exception | None = None


@_dos.ffi.def_extern()
def _pydosmain(_: int, __: list[str]):
    """Called by C function dosmain()."""
    try:
        return _main_fn() or 0
    except Exception as e:
        global _raised_exception
        _raised_exception = e
        return 0


def start(main_fn: MainFunc, argv: list[str] = None) -> int:
    global _main_fn
    global _raised_exception

    if _bg_thread:
        raise RuntimeError('Already running in background')

    _main_fn = main_fn

    if argv is None:
        argv = []
    c_args = [_dos.ffi.new('char[]', arg.encode('utf-8')) for arg in argv]
    c_argv = _dos.ffi.new('char*[]', c_args)
    result = _dos.lib.main(len(argv), c_argv)

    if _raised_exception is not None:
        try:
            raise _raised_exception
        finally:
            _raised_exception = None

    return result


class BackgroundThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{'daemon': True, **kwargs})
        self.ready = threading.Event()
        self.stop = threading.Event()
        self.argv: list[str] | None = None

    def run(self) -> None:
        start(self.main, self.argv)

    def main(self) -> None:
        self.ready.set()
        self.stop.wait()


def run_in_background(argv: list[str] = None):
    global _bg_thread

    if _bg_thread:
        raise RuntimeError('Already running in background')

    thread = BackgroundThread()
    thread.argv = argv
    thread.start()
    thread.ready.wait()
    _bg_thread = thread


def stop():
    global _bg_thread

    if not _bg_thread:
        raise RuntimeError('Not running in the background')
    _bg_thread.stop.set()
    _bg_thread.join()
    _bg_thread = None
