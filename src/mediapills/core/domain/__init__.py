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
from enum import Enum

"""This is text"""

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
