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

from mediapills.core.domain.loggers import BaseLogger
from mediapills.core.domain.outputs import BaseOutput


class BaseUseCase(metaclass=abc.ABCMeta):
    """Contains application specific business rules."""

    def execute(self) -> None:  # dead: disable
        """Perform business logic and change system state."""
        raise NotImplementedError()


class BaseLoggerAwareUseCase(BaseUseCase, metaclass=abc.ABCMeta):
    """Contains application logger interface aware business rules."""

    def __init__(self, logger: BaseLogger):
        """Class constructor."""
        self._logger = logger

    @property
    def logger(self) -> BaseLogger:
        """Property logger getter."""
        return self._logger

    @logger.setter
    def logger(self, logger: BaseLogger) -> None:
        """Property logger getter."""
        self._logger = logger


class BaseOutputAwareUseCase(  # dead: disable
    BaseLoggerAwareUseCase, metaclass=abc.ABCMeta
):
    """Contains application output and logger interface aware business rules."""

    def __init__(self, logger: BaseLogger, output: BaseOutput):
        """Class constructor."""
        super().__init__(logger=logger)
        self._output = output

    @property
    def output(self) -> BaseOutput:
        """Property output getter."""
        return self._output

    @output.setter
    def output(self, output: BaseOutput) -> None:
        """Property output getter."""
        self._output = output
