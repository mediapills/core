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
from abc import ABCMeta
from abc import abstractmethod
from typing import List
from typing import Optional

from mediapills.kernel.core.entities import BaseUUIDAwareEntity


class BaseViewRepository(metaclass=ABCMeta):
    """Well documented way of working with read only data source."""

    def get_one(self, uuid: str) -> Optional[BaseUUIDAwareEntity]:  # dead: disable
        """Retrieve row selected from one or more tables."""
        filtered = filter(lambda entity: entity.uuid == uuid, self.get_all())
        return next(filtered, None)

    @abstractmethod
    def get_all(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> List[BaseUUIDAwareEntity]:
        """Retrieve rows selected from one or more tables."""
        raise NotImplementedError()


class BaseRepository(BaseViewRepository, metaclass=ABCMeta):  # dead: disable
    """Well documented way of working with manageable data source."""

    @abstractmethod  # dead: disable
    def insert(self, entity: BaseUUIDAwareEntity) -> Optional[BaseUUIDAwareEntity]:
        """Insert row into table."""
        raise NotImplementedError()

    @abstractmethod  # dead: disable
    def update(self, entity: BaseUUIDAwareEntity) -> Optional[BaseUUIDAwareEntity]:
        """Update row in table."""
        raise NotImplementedError()

    @abstractmethod  # dead: disable
    def delete(self, uuid: str) -> bool:
        """Delete row from table that satisfy the condition where uuid equal value."""
        raise NotImplementedError()
