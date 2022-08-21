import unittest
from unittest import mock

import dos_like
from dos_like import runner
from tests import helpers


class TestRunner(helpers.PlatformSetter, unittest.TestCase):

    def test_main_fn_is_called(self):
        main = mock.MagicMock()
        dos_like.start(main)
        main.assert_called_once()

    def test_exception_raised_by_main_is_raised_from_start(self):
        exc = Exception()
        main = mock.MagicMock(side_effect=exc)
        with self.assertRaises(Exception) as cm:
            dos_like.start(main)
        self.assertIs(exc, cm.exception)

    def test_run_in_background_raises_runtime_error_if_already_running(self):
        dos_like.run_in_background()
        try:
            with self.assertRaises(RuntimeError):
                dos_like.run_in_background()
        finally:
            dos_like.stop()

    def test_stop_raises_runtime_error_if_not_running(self):
        with self.assertRaises(RuntimeError):
            dos_like.stop()

    def test_start_raises_runtime_error_if_running_in_background(self):
        dos_like.run_in_background()
        main = mock.MagicMock()
        try:
            with self.assertRaises(RuntimeError):
                dos_like.start(main)
        finally:
            dos_like.stop()

    def test_run_in_background_raises_runtime_error_on_macos(self):
        real_is_macos = runner._is_macos
        try:
            runner._is_macos = True
            with self.assertRaises(RuntimeError):
                dos_like.run_in_background()
        finally:
            runner._is_macos = real_is_macos
