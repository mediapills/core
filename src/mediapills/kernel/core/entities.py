# Copyright (c) 2021-2021 Mediapills Kernel.
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
import abc
from datetime import datetime
from enum import Enum
from typing import Optional

"""TODO: add description."""
LOGGING_LEVEL_DEBUG = "debug"

"""TODO: add description."""
LOGGING_LEVEL_INFO = "info"

"""TODO: add description."""
LOGGING_LEVEL_WARN = "warn"

"""TODO: add description."""
LOGGING_LEVEL_ERROR = "error"

"""TODO: add description."""
LOGGING_LEVEL_CRITICAL = "critical"

LOGGING_LEVELS = frozenset(  # dead: disable
    [
        LOGGING_LEVEL_DEBUG,
        LOGGING_LEVEL_INFO,
        LOGGING_LEVEL_WARN,
        LOGGING_LEVEL_ERROR,
        LOGGING_LEVEL_CRITICAL,
    ]
)


class LoggingLevel(Enum):
    """Enumerated logging constants."""

    DEBUG = LOGGING_LEVEL_DEBUG
    INFO = LOGGING_LEVEL_INFO
    WARN = LOGGING_LEVEL_WARN
    ERROR = LOGGING_LEVEL_ERROR
    CRITICAL = LOGGING_LEVEL_CRITICAL


class BaseEntity(metaclass=abc.ABCMeta):
    """Encapsulate Enterprise wide business rules."""

    pass


class LogRecordEntity(BaseEntity):  # dead: disable
    """Information about a logging event."""

    __slots__ = ["_msg", "_name", "_lvl", "_created", "_thread"]

    def __init__(
        self, msg: str, lvl: LoggingLevel, name: str, created: Optional[datetime] = None
    ):
        """Log Record constructor."""
        self._msg = msg
        self._lvl = lvl
        self._name = name
        self._created = created

    @property
    def msg(self) -> str:
        """Log message."""
        return self._msg

    @property
    def lvl(self) -> LoggingLevel:
        """Numeric logging level for the message."""
        return self._lvl

    @property
    def name(self) -> str:
        """Name of the logger (logging channel)."""
        return self._name

    @property
    def created(self) -> Optional[datetime]:
        """Time when the log record was created."""
        return self._created
