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
"""This module implements classes with BaseLogger interface."""
import logging
import sys
import typing as t

from mediapills.core.domain.entities import LoggingLevel
from mediapills.core.domain.loggers import BaseLogger


class PythonLoggerAdapter(BaseLogger):  # dead: disable
    """Python logging Adapter to BaseLogger interface."""

    def __init__(self, level: int = logging.INFO):
        """Class constructor."""
        # TODO add logging formatters manager

        logging.basicConfig(stream=sys.stdout, level=level)
        logger = logging.getLogger(__name__)
        self._logger = logger

    def log(
        self,
        lvl: LoggingLevel,
        msg: str,
        *args: t.List[t.Any],
        **kwargs: t.Dict[str, t.Any]
    ) -> None:
        """General logging method."""
        self._logger.log(lvl.value, msg, *args, **kwargs)  # type: ignore

    def debug(
        self, msg: str, *args: t.List[t.Any], **kwargs: t.Dict[str, t.Any]
    ) -> None:
        """Log a message with level DEBUG on this logger."""
        self._logger.debug(msg, *args, **kwargs)  # type: ignore

    def info(
        self, msg: str, *args: t.List[t.Any], **kwargs: t.Dict[str, t.Any]
    ) -> None:
        """Log a message with level INFO on this logger."""
        self._logger.info(msg, *args, **kwargs)  # type: ignore

    def warn(
        self, msg: str, *args: t.List[t.Any], **kwargs: t.Dict[str, t.Any]
    ) -> None:
        """Log a message with level WARN on this logger."""
        self._logger.warn(msg, *args, **kwargs)  # type: ignore

    def warning(
        self, msg: str, *args: t.List[t.Any], **kwargs: t.Dict[str, t.Any]
    ) -> None:
        """Log a message with level WARN alias."""
        self._logger.warning(msg, *args, **kwargs)  # type: ignore

    def error(
        self, msg: str, *args: t.List[t.Any], **kwargs: t.Dict[str, t.Any]
    ) -> None:
        """Log a message with level ERROR on this logger."""
        self._logger.error(msg, *args, **kwargs)  # type: ignore

    def critical(
        self, msg: str, *args: t.List[t.Any], **kwargs: t.Dict[str, t.Any]
    ) -> None:
        """Log a message with level CRITICAL on this logger."""
        self._logger.critical(msg, *args, **kwargs)  # type: ignore
