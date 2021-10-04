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
import abc
import typing as t
from enum import Enum

from mediapills.core.domain.outputs import BaseOutput

"""The request succeeded."""
HTTP_RESPONSE_STATUS_CODE_OK = 200

"""The request succeeded, and a new resource created as a result."""
HTTP_RESPONSE_STATUS_CODE_CREATED = 201

"""There is no content to send for this request, but the headers may be useful."""
HTTP_RESPONSE_STATUS_CODE_NO_CONTENT = 204

"""This response code means that the URI of requested resource has been changed
temporarily.
"""
HTTP_RESPONSE_STATUS_CODE_FOUND = 302

"""The server could not understand the request due to invalid syntax."""
HTTP_RESPONSE_STATUS_CODE_BAD_REQUEST = 400

"""Although the HTTP standard specifies 'unauthorized', semantically this
response means 'unauthenticated'.
"""
HTTP_RESPONSE_STATUS_CODE_UNAUTHORIZED = 401

"""The client does not have access rights to the content; that is, it is
unauthorized, so the server is refusing to give the requested resource.
"""
HTTP_RESPONSE_STATUS_CODE_FORBIDDEN = 403

"""The server can not find the requested resource. In the browser, this means
the URL is not recognized.
"""
HTTP_RESPONSE_STATUS_CODE_NOT_FOUND = 404

"""This response is sent when a request conflicts with the current state of the
server.
"""
HTTP_RESPONSE_STATUS_CODE_CONFLICT = 409

"""The request was well-formed but was unable to be followed due to semantic errors."""
HTTP_RESPONSE_STATUS_CODE_ENTITY = 422

# Server error responses codes group

"""The server has encountered a situation it does not know how to handle."""
HTTP_RESPONSE_STATUS_CODE_INTERNAL_SERVER_ERROR = 500


"""Information response code group."""
HTTP_RESPONSE_STATUS_CODES_INFORMATIONAL: t.FrozenSet[t.List[int]] = frozenset([])

"""Successful response code group."""
HTTP_RESPONSE_STATUS_CODES_SUCCESSFUL = frozenset(
    [
        HTTP_RESPONSE_STATUS_CODE_OK,
        HTTP_RESPONSE_STATUS_CODE_CREATED,
        HTTP_RESPONSE_STATUS_CODE_NO_CONTENT,
    ]
)

"""Successful response code group."""
HTTP_RESPONSE_STATUS_CODE_REDIRECTIONS = frozenset([HTTP_RESPONSE_STATUS_CODE_FOUND])

"""Client Error response code group."""
HTTP_RESPONSE_STATUS_CODE_CLIENT_ERRORS = frozenset(
    [
        HTTP_RESPONSE_STATUS_CODE_BAD_REQUEST,
        HTTP_RESPONSE_STATUS_CODE_UNAUTHORIZED,
        HTTP_RESPONSE_STATUS_CODE_FORBIDDEN,
        HTTP_RESPONSE_STATUS_CODE_NOT_FOUND,
        HTTP_RESPONSE_STATUS_CODE_CONFLICT,
        HTTP_RESPONSE_STATUS_CODE_ENTITY,
    ]
)

"""Client Error response code group."""
HTTP_RESPONSE_STATUS_CODE_SERVER_ERRORS = frozenset(
    [HTTP_RESPONSE_STATUS_CODE_INTERNAL_SERVER_ERROR]
)

"""All available HTTP response codes."""
HTTP_RESPONSE_STATUS_CODES = frozenset(  # dead: disable
    [
        *HTTP_RESPONSE_STATUS_CODES_INFORMATIONAL,
        *HTTP_RESPONSE_STATUS_CODES_SUCCESSFUL,
        *HTTP_RESPONSE_STATUS_CODE_REDIRECTIONS,
        *HTTP_RESPONSE_STATUS_CODE_CLIENT_ERRORS,
        *HTTP_RESPONSE_STATUS_CODE_SERVER_ERRORS,
    ]
)


class HTTPResponseStatus(Enum):
    """Enumerated HTTP response codes constants."""

    OK = HTTP_RESPONSE_STATUS_CODE_OK  # dead: disable
    CREATED = HTTP_RESPONSE_STATUS_CODE_CREATED  # dead: disable
    NO_CONTENT = HTTP_RESPONSE_STATUS_CODE_NO_CONTENT  # dead: disable
    FOUND = HTTP_RESPONSE_STATUS_CODE_FOUND  # dead: disable
    BAD_REQUEST = HTTP_RESPONSE_STATUS_CODE_BAD_REQUEST  # dead: disable
    UNAUTHORIZED = HTTP_RESPONSE_STATUS_CODE_UNAUTHORIZED  # dead: disable
    FORBIDDEN = HTTP_RESPONSE_STATUS_CODE_FORBIDDEN  # dead: disable
    NOT_FOUND = HTTP_RESPONSE_STATUS_CODE_NOT_FOUND  # dead: disable
    CONFLICT = HTTP_RESPONSE_STATUS_CODE_CONFLICT  # dead: disable
    ENTITY = HTTP_RESPONSE_STATUS_CODE_ENTITY  # dead: disable
    SERVER_ERROR = HTTP_RESPONSE_STATUS_CODE_INTERNAL_SERVER_ERROR  # dead: disable


class BaseHTTPResponse(BaseOutput, metaclass=abc.ABCMeta):  # dead: disable
    """Response content made by a named host, to a client."""

    @property  # type: ignore
    @abc.abstractmethod
    def status(self) -> HTTPResponseStatus:
        """HTTP status code getter."""
        raise NotImplementedError()

    @status.setter  # type: ignore
    @abc.abstractmethod
    def status(self, value: HTTPResponseStatus) -> None:
        """HTTP status code setter."""
        raise NotImplementedError()

    @property  # type: ignore
    @abc.abstractmethod
    def headers(self) -> t.Dict[str, str]:
        """Headers property getter."""
        raise NotImplementedError()

    @headers.setter  # type: ignore
    @abc.abstractmethod
    def headers(self, headers: t.Dict[str, str]) -> None:
        """Headers property setter."""
        raise NotImplementedError()

    @property  # type: ignore
    @abc.abstractmethod
    def cookies(self) -> t.Dict[str, str]:
        """Cookies property getter."""
        raise NotImplementedError()

    @cookies.setter  # type: ignore
    @abc.abstractmethod
    def cookies(self, cookie: t.Dict[str, str]) -> None:
        """Cookies property setter."""
        raise NotImplementedError()
