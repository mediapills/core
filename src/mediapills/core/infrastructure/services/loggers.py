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
import logging
import sys
import typing as T
from enum import Enum

from mediapills.core.domain import LoggingLevel as BaseLoggingLevel
from mediapills.core.domain.services.loggers import BaseLogger

"""This module implements classes with BaseLogger interface."""


class LoggingLevel(Enum):
    """Enumerated logging levels for standardized log message categorization."""

    LOGGING_LEVEL_DEBUG = 10
    LOGGING_LEVEL_INFO = 20
    LOGGING_LEVEL_WARN = 30
    LOGGING_LEVEL_ERROR = 40
    LOGGING_LEVEL_CRITICAL = 50


class PythonLoggerAdapter(BaseLogger):  # dead: disable
    """Python logging Adapter to BaseLogger interface."""

    def __init__(self, level: int = logging.INFO):
        """Class constructor."""
        # TODO add logging formatters manager

        logging.basicConfig(stream=sys.stdout, level=level)
        logger = logging.getLogger(__name__)
        self._logger = logger

    def log(
        self, lvl: BaseLoggingLevel, msg: str, *args: T.Any, **kwargs: T.Any
    ) -> None:
        """General logging method."""
        self._logger.log(LoggingLevel[lvl.value].value, msg, *args, **kwargs)

    def debug(self, msg: str, *args: T.Any, **kwargs: T.Any) -> None:
        """Log a message with level DEBUG on this logger."""
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args: T.Any, **kwargs: T.Any) -> None:
        """Log a message with level INFO on this logger."""
        self._logger.info(msg, *args, **kwargs)

    def warn(self, msg: str, *args: T.Any, **kwargs: T.Any) -> None:
        """Log a message with level WARN on this logger."""
        self._logger.warn(msg, *args, **kwargs)

    def warning(self, msg: str, *args: T.Any, **kwargs: T.Any) -> None:
        """Log a message with level WARN alias."""
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args: T.Any, **kwargs: T.Any) -> None:
        """Log a message with level ERROR on this logger."""
        self._logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args: T.Any, **kwargs: T.Any) -> None:
        """Log a message with level CRITICAL on this logger."""
        self._logger.critical(msg, *args, **kwargs)
