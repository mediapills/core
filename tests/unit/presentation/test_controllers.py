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

from mediapills.core.presentation.controllers import BaseController


class _EchoController(BaseController):
    """Minimal concrete controller for exercising the base type."""

    def run(self, payload: str) -> str:
        return f"ok:{payload}"


class TestBaseController(unittest.TestCase):
    def test_base_controller_is_instantiable_extension_point(self) -> None:
        controller = BaseController()
        self.assertIsInstance(controller, BaseController)

    def test_subclass_can_implement_application_behavior(self) -> None:
        controller = _EchoController()
        self.assertEqual("ok:ping", controller.run("ping"))
