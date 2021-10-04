# Copyright (c) 2021-2021 Mediapills Core.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import unittest
from unittest.mock import Mock

from mediapills.core.loggers import PythonLoggerAdapter


class TestPythonLoggerAdapter(unittest.TestCase):
    @property
    def mock_logger(self) -> PythonLoggerAdapter:
        python_logger = PythonLoggerAdapter()
        python_logger._logger = Mock()

        return python_logger

    def test_debug_should_call_logger_debug(self) -> None:
        python_logger = self.mock_logger
        python_logger.debug("test")
        python_logger._logger.debug.assert_called_once_with("test")  # type: ignore

    def test_info_should_call_logger_info(self) -> None:
        python_logger = self.mock_logger
        python_logger.info("test")
        python_logger._logger.info.assert_called_once_with("test")  # type: ignore

    def test_warn_should_call_logger_warn(self) -> None:
        python_logger = self.mock_logger
        python_logger.warn("test")
        python_logger._logger.warn.assert_called_once_with("test")  # type: ignore

    def test_warning_should_call_logger_warning(self) -> None:
        python_logger = self.mock_logger
        python_logger.warning("test")
        python_logger._logger.warning.assert_called_once_with("test")  # type: ignore

    def test_error_should_call_logger_error(self) -> None:
        python_logger = self.mock_logger
        python_logger.error("test")
        python_logger._logger.error.assert_called_once_with("test")  # type: ignore
