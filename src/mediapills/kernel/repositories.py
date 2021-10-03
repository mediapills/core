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
import os
import sys
from typing import List
from typing import Optional

from mediapills.kernel.core.entities import KeyValueEntity
from mediapills.kernel.core.repositories import BaseViewRepository


class EnvironRepository(  # dead: disable
    BaseViewRepository  # type: ignore
):
    """Environment variables read only repository."""

    def get_one(self, uuid: str) -> Optional[KeyValueEntity]:  # dead: disable
        """Retrieve environment variable by name."""
        if sys.platform == "win32":
            uuid = uuid.upper()  # pragma: no cover
        val = os.getenv(uuid)

        return None if val is None else KeyValueEntity(uuid=uuid, val=val)

    def get_all(
        self, limit: Optional[int] = None, offset: Optional[int] = None  # dead: disable
    ) -> List[KeyValueEntity]:
        """Retrieve all environment variables."""
        items = dict(os.environ).items()
        return [KeyValueEntity(uuid=k, val=v) for k, v in items]
