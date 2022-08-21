import sys
import unittest
import warnings

from dos_like import runner


class PlatformSetter(unittest.TestCase):
    """Disable macOS background thread check for headless macOS tests.

    Tests won't run with a real GUI in macOS because they call GUI functions in
    a background thread.  We can disable this check if we're running in
    headless mode (NULL_PLATFORM).

    """

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        if sys.platform == 'darwin':
            warnings.warn(
                'Running tests on macOS, assuming _dos has been compiled with '
                '-DNULL_PLATFORM')
            cls.__is_macos = runner._is_macos
            runner._is_macos = False

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        if hasattr(cls, '__is_macos'):
            runner._is_macos = cls.__is_macos
