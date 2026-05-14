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
import os
import sys
import typing as t

from mediapills.core.domain.entities import KeyValueEntity
from mediapills.core.domain.repositories import BaseRepository


class DictRepositoryAdapter(BaseRepository):
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

    def get_all(  # type: ignore[override]
        self,
        limit: t.Optional[int] = None,
        offset: t.Optional[int] = None,
    ) -> t.List[KeyValueEntity]:
        """Retrieve dict data, optionally paginated by insertion order."""
        pairs = self._slice_items(self._data.items(), limit=limit, offset=offset)
        return [KeyValueEntity(uuid=k, val=v) for k, v in pairs]


class EnvironRepository(BaseRepository):  # dead: disable
    """Environment variables read only repository."""

    def get_one(self, uuid: str) -> t.Optional[KeyValueEntity]:  # dead: disable
        """Retrieve environment variable by name."""
        if sys.platform == "win32":
            uuid = uuid.upper()  # pragma: no cover
        val = os.environ.get(uuid)

        return None if val is None else KeyValueEntity(uuid=uuid, val=val)

    def get_all(  # type: ignore[override]
        self,
        limit: t.Optional[int] = None,
        offset: t.Optional[int] = None,
    ) -> t.List[KeyValueEntity]:
        """Return env vars as entities; optional limit/offset (environ order)."""
        pairs = self._slice_items(os.environ.items(), limit=limit, offset=offset)
        return [KeyValueEntity(uuid=k, val=v) for k, v in pairs]
