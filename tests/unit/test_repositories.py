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
import sys
import unittest
from unittest.mock import patch

from mediapills.kernel.repositories import EnvironRepository

_MODULE_LOCATION_OS_ENVIRON_ = "mediapills.kernel.repositories.os.environ"


class TestEnvironRepository(unittest.TestCase):
    MOCK_ENVIRON = {"key": "value"}
    MOCK_ENVIRON_LOWER_CASE = {"lower_case_key": "lower_case_value"}
    MOCK_ENVIRON_UPPER_CASE = {"UPPER_CASE_KEY": "upper_case_value"}

    @patch(_MODULE_LOCATION_OS_ENVIRON_, MOCK_ENVIRON)
    def test_find_one_should_return_one(self) -> None:
        repo = EnvironRepository()
        obj = repo.get_one("key")

        self.assertEqual("value", obj.value)

    @patch(_MODULE_LOCATION_OS_ENVIRON_, MOCK_ENVIRON)
    def test_find_all_should_return_all(self) -> None:
        repo = EnvironRepository()
        data = repo.get_all()
        key = "key"
        # TODO must work in library not tests (move this if in lib)
        if sys.platform == "win32":
            key = "KEY"

        self.assertEqual(1, len(data))
        self.assertEqual(key, data[0].uuid)

    def test_find_one_wrong_key_should_return_none(self) -> None:
        repo = EnvironRepository()
        val = repo.get_one("wrong_key")

        self.assertIsNone(val)

    # TODO check if sys.platform can help here for win
    @unittest.skipIf(sys.platform == "win32", reason="does not run on windows")
    @patch(_MODULE_LOCATION_OS_ENVIRON_, MOCK_ENVIRON_LOWER_CASE)
    def test_get_one_should_handle_lower_case_sensitivity(self) -> None:
        repo = EnvironRepository()
        obj = repo.get_one("lower_case_key")

        self.assertIsNotNone(obj)
        self.assertEqual("lower_case_value", obj.value)
        self.assertIsNone(repo.get_one("LOWER_CASE_KEY"))

    # TODO check if sys.platform can help here for win
    @unittest.skipIf(sys.platform == "win32", reason="does not run on windows")
    @patch(_MODULE_LOCATION_OS_ENVIRON_, MOCK_ENVIRON_UPPER_CASE)
    def test_get_one_should_handle_upper_case_sensitivity(self) -> None:
        repo = EnvironRepository()
        obj = repo.get_one("UPPER_CASE_KEY")

        self.assertIsNotNone(obj)
        self.assertEqual("upper_case_value", obj.value)
        self.assertIsNone(repo.get_one("upper_case_key"))
