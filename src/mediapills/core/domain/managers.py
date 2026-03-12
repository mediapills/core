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
from abc import ABCMeta
from abc import abstractmethod

from mediapills.core.domain.entities import BaseImmutableEntity
from mediapills.core.domain.entities import BaseMutableEntity
from mediapills.core.domain.entities import BaseUniqueEntity
from mediapills.core.domain.repositories import BaseRepository


class ImmutableEntityManager(metaclass=ABCMeta):
    """EntityManager for entities that support insert-only (immutable) operations."""

    @abstractmethod
    def repository(self) -> BaseRepository:  # dead: disable
        """Get the repository instance associated with this manager."""
        pass

    @abstractmethod
    def insert(self, entity: BaseImmutableEntity) -> BaseUniqueEntity:  # dead: disable
        """Insert a new entity."""
        raise NotImplementedError()


class MutableEntityManager(ImmutableEntityManager, metaclass=ABCMeta):
    """EntityManager for entities that support insert and update (mutable) operations."""

    @abstractmethod
    def update(self, entity: BaseMutableEntity) -> BaseUniqueEntity:  # dead: disable
        """Update an existing entity."""
        raise NotImplementedError()


class PersistentEntityManager(MutableEntityManager, metaclass=ABCMeta):  # dead: disable
    """Manager for entities that support full CRUD (insert, update, delete) operations."""

    @abstractmethod
    def delete(self, uuid: str) -> bool:  # dead: disable
        """Delete an entity by its unique identifier."""
        raise NotImplementedError()
