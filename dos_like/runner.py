from __future__ import annotations

import threading
from typing import Callable, Optional

try:
    from typing import TypeAlias  # type: ignore
except ImportError:  # pragma: no cover
    from typing_extensions import TypeAlias  # type: ignore

from dos_like import _dos

MainFunc: TypeAlias = Callable[[], Optional[int]]
"""dos-like python main function."""

_bg_thread: BackgroundThread | None = None
_main_fn: MainFunc | None = None
_raised_exception: Exception | None = None


@_dos.ffi.def_extern()
def _pydosmain(_: int, __: list[str]) -> int:
    """Called by C function dosmain()."""
    assert _main_fn is not None
    try:
        return _main_fn() or 0
    except Exception as e:
        global _raised_exception
        _raised_exception = e
        return 0


def start(main_fn: MainFunc, argv: list[str] = None) -> int:
    """Start dos-like with a given main function, blocking until it returns.

    :param main_fn: Run this function in dos-like.  Inside this function,
        :mod:`dos_like.dos` functions may be called.
    :param argv: optional arguments to pass to dos-like.  Notably, ``-w``
        starts in windowed mode.
    :return: value returned by **main_fn**
    :raises RuntimeError: if already running

    """
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


def run_in_background(argv: list[str] = None) -> None:
    """Start dos-like in a background thread and return immediately.

    :param argv: optional arguments to pass to dos-like.  Notably, ``-w``
        starts in windowed mode.

    Once returned, :mod:`dos_like.dos` functions may be called.

    """
    global _bg_thread

    if _bg_thread:
        raise RuntimeError('Already running in background')

    thread = BackgroundThread()
    thread.argv = argv
    thread.start()
    thread.ready.wait()
    _bg_thread = thread


def stop() -> None:
    """Stop running the background thread started by :func:`run_in_background`.

    :raises RuntimeError: if not running in the background

    """
    global _bg_thread

    if not _bg_thread:
        raise RuntimeError('Not running in the background')
    _bg_thread.stop.set()
    _bg_thread.join()
    _bg_thread = None
