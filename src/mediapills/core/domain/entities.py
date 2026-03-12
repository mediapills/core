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
import abc
from datetime import datetime
from enum import Enum
from typing import Any
from typing import Optional

# Logging level constants with clear, professional docstrings.

"""Diagnostic information useful for debugging, intended for developers and advanced
users."""
LOGGING_LEVEL_DEBUG = "debug"

"""General operational events, such as service start/stop or configuration assumptions.
"""
LOGGING_LEVEL_INFO = "info"

"""Non-fatal issues that may cause unexpected behavior but do not stop the application.
"""
LOGGING_LEVEL_WARN = "warn"

"""Errors that are fatal to a specific operation but not to the overall service or
application."""
LOGGING_LEVEL_ERROR = "error"

"""Severe errors that require immediate attention and may force a shutdown to prevent data
loss."""
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
"""A set of all supported logging levels."""


class LoggingLevel(Enum):
    """Enumerated logging levels for standardized log message categorization."""

    DEBUG = LOGGING_LEVEL_DEBUG
    INFO = LOGGING_LEVEL_INFO
    WARN = LOGGING_LEVEL_WARN
    ERROR = LOGGING_LEVEL_ERROR
    CRITICAL = LOGGING_LEVEL_CRITICAL


class BaseEntity(metaclass=abc.ABCMeta):
    """Abstract base class representing a domain entity encapsulating business rules."""

    pass


class BaseUniqueEntity(BaseEntity, metaclass=abc.ABCMeta):
    """Abstract base class for entities with a unique UUID property."""

    __slots__ = ["_uuid"]

    def __init__(self, uuid: str):
        """
        Initialize the entity with a unique identifier.

        Args:
            uuid (str): The unique identifier for the entity.
        """
        self._uuid = uuid

    @property
    def uuid(self) -> str:
        """
        Get the UUID of the entity.

        Returns:
            str: The unique identifier.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str) -> None:
        """
        Set the UUID of the entity.

        Args:
            uuid (str): The new unique identifier.
        """
        self._uuid = uuid


class BaseImmutableEntity(BaseUniqueEntity, metaclass=abc.ABCMeta):
    """Abstract base class for immutable entities with a unique identifier."""

    __slots__ = ["_created_at"]

    def __init__(self, uuid: str):
        """Initialize the immutable entity."""
        super().__init__(uuid=uuid)


class BaseMutableEntity(BaseImmutableEntity, metaclass=abc.ABCMeta):
    """Abstract base class for mutable entities with a unique identifier."""

    __slots__ = ["_created_at", "_updated_at"]

    def __init__(self, uuid: str, val: Any):
        """Initialize the mutable entity."""
        super().__init__(uuid=uuid)
        self._value = val


class KeyValueEntity(BaseUniqueEntity):
    """Entity representing a key-value pair, suitable for key-value storage systems."""

    __slots__ = ["_uuid", "_value"]

    def __init__(self, uuid: str, val: Any):
        """
        Initialize the key-value entity.

        Args:
            uuid (str): The unique identifier for the entity.
            val (Any): The value associated with the key.
        """
        super().__init__(uuid=uuid)
        self._value = val

    @property
    def value(self) -> Any:
        """
        Get the value associated with the entity.

        Returns:
            Any: The value.
        """
        return self._value

    @value.setter
    def value(self, val: Any) -> None:
        """
        Set the value associated with the entity.

        Args:
            val (Any): The new value.
        """
        self._value = val


class LogRecordEntity(BaseEntity):  # dead: disable
    """
    Entity representing a log record for application logging.

    Includes message, level, logger name, and timestamp.
    """

    __slots__ = ["_msg", "_name", "_lvl", "_created", "_thread"]

    def __init__(
        self, msg: str, lvl: LoggingLevel, name: str, created: Optional[datetime] = None
    ):
        """
        Initialize the log record entity.

        Args:
            msg (str): The log message.
            lvl (LoggingLevel): The logging level.
            name (str): The name of the logger or logging channel.
            created (Optional[datetime]): The timestamp when the log was created.
        """
        self._msg = msg
        self._lvl = lvl
        self._name = name
        self._created = created

    @property
    def msg(self) -> str:
        """
        Get the log message.

        Returns:
            str: The log message.
        """
        return self._msg

    @property
    def lvl(self) -> LoggingLevel:
        """
        Get the logging level for the message.

        Returns:
            LoggingLevel: The logging level.
        """
        return self._lvl

    @property
    def name(self) -> str:
        """
        Get the name of the logger or logging channel.

        Returns:
            str: The logger name.
        """
        return self._name

    @property
    def created(self) -> Optional[datetime]:
        """
        Get the timestamp when the log record was created.

        Returns:
            Optional[datetime]: The creation time, if available.
        """
        return self._created
