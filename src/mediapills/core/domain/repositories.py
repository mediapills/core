# Copyright (c) 2021-2026 Mediapills Core.
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
import typing as t
from abc import ABCMeta
from abc import abstractmethod

from mediapills.core.domain.entities import BaseUniqueEntity


class BaseViewRepository(metaclass=ABCMeta):
    """Well documented way of working with read only data source."""

    @staticmethod
    def _slice_items(
        items: t.Iterable[t.Tuple[str, t.Any]],
        limit: t.Optional[int],
        offset: t.Optional[int],
    ) -> t.List[t.Tuple[str, t.Any]]:
        """Apply limit/offset over an ordered sequence of (key, value) pairs."""
        seq = list(items)
        start = 0 if offset is None else max(offset, 0)
        if limit is None:
            return seq[start:]
        end = start + max(limit, 0)
        return seq[start:end]

    def get_one(self, uuid: str) -> t.Optional[BaseUniqueEntity]:  # dead: disable
        """Retrieve row selected from one or more tables."""
        filtered = filter(lambda entity: entity.uuid == uuid, self.get_all())
        return next(filtered, None)

    @abstractmethod
    def get_all(
        self, limit: t.Optional[int] = None, offset: t.Optional[int] = None
    ) -> t.List[BaseUniqueEntity]:
        """Retrieve rows selected from one or more tables."""
        raise NotImplementedError()


class BaseRepository(BaseViewRepository, metaclass=ABCMeta):
    """Well documented way of working with manageable data source."""

    @abstractmethod
    def insert(  # dead: disable
        self, entity: BaseUniqueEntity
    ) -> t.Optional[BaseUniqueEntity]:
        """Insert row into table."""
        raise NotImplementedError()

    @abstractmethod
    def update(  # dead: disable
        self, entity: BaseUniqueEntity
    ) -> t.Optional[BaseUniqueEntity]:
        """Update row in table."""
        raise NotImplementedError()

    @abstractmethod
    def delete(self, uuid: str) -> bool:  # dead: disable
        """Delete row from table that satisfy the condition where uuid equal value."""
        raise NotImplementedError()
