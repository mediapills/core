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
import unittest

from mediapills.core.domain.entities import KeyValueEntity
from mediapills.core.persistence.managers import DictEntityManagerAdapter


class TestDictEntityManagerAdapter(unittest.TestCase):
    def test_insert_should_add(self) -> None:
        em = DictEntityManagerAdapter({})
        record = KeyValueEntity(uuid="new", val="inserted")
        returned = em.insert(record)

        self.assertIs(returned, record)
        self.assertEqual(1, len(em.repository.get_all()))
        stored = em.repository.get_one("new")
        self.assertIsNotNone(stored)
        self.assertEqual("inserted", stored.value)

    def test_insert_should_raise_when_uuid_exists(self) -> None:
        em = DictEntityManagerAdapter({"key": "existing"})
        with self.assertRaises(KeyError):
            em.insert(KeyValueEntity(uuid="key", val="other"))

    def test_update_should_replace(self) -> None:
        em = DictEntityManagerAdapter({"key": "val"})
        record = KeyValueEntity(uuid="key", val="replaced")
        returned = em.update(record)

        self.assertIs(returned, record)
        stored = em.repository.get_one("key")
        self.assertIsNotNone(stored)
        self.assertEqual("replaced", stored.value)

    def test_update_should_raise_when_uuid_missing(self) -> None:
        em = DictEntityManagerAdapter({})
        with self.assertRaises(KeyError):
            em.update(KeyValueEntity(uuid="missing", val="x"))

    def test_delete_should_remove(self) -> None:
        em = DictEntityManagerAdapter({"key": "val"})

        self.assertTrue(em.delete("key"))
        self.assertEqual(0, len(em.repository.get_all()))

    def test_delete_should_skip(self) -> None:
        em = DictEntityManagerAdapter()

        self.assertFalse(em.delete("key"))
