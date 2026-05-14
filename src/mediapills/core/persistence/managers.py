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

from mediapills.core.domain.entities import KeyValueEntity
from mediapills.core.domain.managers import PersistentEntityManager
from mediapills.core.persistence.repositories import DictRepositoryAdapter


class DictEntityManagerAdapter(PersistentEntityManager):  # dead: disable
    """Manager for KeyValueEntity entities that support full CRUD (insert, update,
    delete) operations.
    """

    def __init__(self, data: t.Optional[t.Dict[str, t.Any]] = None):
        """Class constructor."""
        super().__init__()
        self._data = data or {}
        self._repository = None  # type: t.Optional[DictRepositoryAdapter]

    @property
    def repository(self) -> DictRepositoryAdapter:  # dead: disable
        """Get the repository instance associated with this manager."""
        if self._repository is None:
            self._repository = DictRepositoryAdapter(self._data)

        return self._repository

    def insert(  # dead: disable
        self, entity: KeyValueEntity  # type: ignore
    ) -> KeyValueEntity:
        """Insert a new entity."""
        if entity.uuid in self._data:
            raise KeyError(entity.uuid)

        self._data[entity.uuid] = entity.value
        return entity

    def update(  # dead: disable
        self, entity: KeyValueEntity  # type: ignore
    ) -> KeyValueEntity:
        """Update an existing entity."""
        if entity.uuid not in self._data:
            raise KeyError(entity.uuid)

        self._data[entity.uuid] = entity.value
        return entity

    def delete(self, uuid: str) -> bool:  # dead: disable
        """Delete an entity by its unique identifier."""
        if uuid not in self._data:
            return False

        del self._data[uuid]
        return True
