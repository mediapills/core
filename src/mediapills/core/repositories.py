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
import os
import sys
import typing as t

from mediapills.core.domain.entities import KeyValueEntity
from mediapills.core.domain.repositories import BaseRepository
from mediapills.core.domain.repositories import BaseViewRepository


class DictRepositoryAdapter(BaseRepository):  # dead: disable
    """Dictionary variables repository adapter."""

    def __init__(self, data: t.Optional[t.Dict[str, t.Any]] = None):
        """Class constructor."""
        super().__init__()
        self._data = data or {}

    def get_one(self, uuid: str) -> t.Optional[KeyValueEntity]:  # dead: disable
        """Retrieve dict element if exists."""
        if uuid not in self._data:
            return None

        return KeyValueEntity(uuid=uuid, val=self._data.get(uuid, None))

    def get_all(  # type: ignore
        self,
        limit: t.Optional[int] = None,  # dead: disable
        offset: t.Optional[int] = None,  # dead: disable
    ) -> t.List[KeyValueEntity]:
        """Retrieve all dict data."""
        return [KeyValueEntity(uuid=k, val=v) for k, v in self._data.items()]

    def insert(  # type: ignore  # dead: disable
        self, entity: KeyValueEntity
    ) -> t.Optional[KeyValueEntity]:
        """Insert row into table."""
        if entity.uuid in self._data:
            raise KeyError()

        self._data[entity.uuid] = entity.value
        return entity

    def update(  # type: ignore  # dead: disable
        self, entity: KeyValueEntity
    ) -> t.Optional[KeyValueEntity]:
        """Update row in table."""
        if entity.uuid not in self._data:
            raise KeyError()

        self._data[entity.uuid] = entity.value
        return entity

    def delete(self, uuid: str) -> bool:  # dead: disable
        """Delete row from table that satisfy the condition where uuid equal value."""
        if uuid not in self._data:
            return False

        del self._data[uuid]
        return True


class EnvironRepository(BaseViewRepository):  # dead: disable
    """Environment variables read only repository."""

    def get_one(self, uuid: str) -> t.Optional[KeyValueEntity]:  # dead: disable
        """Retrieve environment variable by name."""
        if sys.platform == "win32":
            uuid = uuid.upper()  # pragma: no cover
        val = os.getenv(uuid)

        return None if val is None else KeyValueEntity(uuid=uuid, val=val)

    def get_all(  # type: ignore
        self,
        limit: t.Optional[int] = None,  # dead: disable
        offset: t.Optional[int] = None,  # dead: disable
    ) -> t.List[KeyValueEntity]:
        """Retrieve all environment variables."""
        items = dict(os.environ).items()
        return [KeyValueEntity(uuid=k, val=v) for k, v in items]
