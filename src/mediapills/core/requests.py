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
from enum import Enum
from typing import Dict

"""Requests a representation of the specified resource."""
HTTP_REQUEST_METHOD_GET = "GET"

"""Identical to a GET request, but without the response body."""
HTTP_REQUEST_METHOD_HEAD = "HEAD"

"""Submits an entity to the specified resource."""
HTTP_REQUEST_METHOD_POST = "POST"

"""Replaces all current representations of the target resource."""
HTTP_REQUEST_METHOD_PUT = "PUT"

"""The DELETE method deletes the specified resource."""
HTTP_REQUEST_METHOD_DELETE = "DELETE"

"""Establishes a tunnel to the server identified by the target resource."""
HTTP_REQUEST_METHOD_CONNECT = "CONNECT"

"""Describes the communication options for the target resource."""
HTTP_REQUEST_METHOD_OPTIONS = "OPTIONS"

"""Applies partial modifications to a resource."""
HTTP_REQUEST_METHOD_PATCH = "PATCH"

"""HTTP defined request methods set."""
HTTP_REQUEST_METHODS = frozenset(  # dead: disable
    [
        HTTP_REQUEST_METHOD_GET,
        HTTP_REQUEST_METHOD_HEAD,
        HTTP_REQUEST_METHOD_POST,
        HTTP_REQUEST_METHOD_PUT,
        HTTP_REQUEST_METHOD_DELETE,
        HTTP_REQUEST_METHOD_CONNECT,
        HTTP_REQUEST_METHOD_OPTIONS,
        HTTP_REQUEST_METHOD_PATCH,
    ]
)


class HTTPRequestMethod(Enum):
    """Enumerated HTTP method constants."""

    GET = HTTP_REQUEST_METHOD_GET  # dead: disable
    HEAD = HTTP_REQUEST_METHOD_HEAD  # dead: disable
    POST = HTTP_REQUEST_METHOD_POST  # dead: disable
    PUT = HTTP_REQUEST_METHOD_PUT  # dead: disable
    DELETE = HTTP_REQUEST_METHOD_DELETE  # dead: disable
    CONNECT = HTTP_REQUEST_METHOD_CONNECT  # dead: disable
    OPTIONS = HTTP_REQUEST_METHOD_OPTIONS  # dead: disable
    PATCH = HTTP_REQUEST_METHOD_PATCH  # dead: disable


class BaseHTTPRequest(metaclass=abc.ABCMeta):  # dead: disable
    """Request content made by a client, to a named host."""

    @property
    @abc.abstractmethod
    def url(self) -> str:  # dead: disable
        """Uniform Resource Locator, colloquially termed a web address."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def uri(self) -> str:  # dead: disable
        """Uniform Resource Identifier is a unique sequence of characters that
        identifies a logical or physical resource.
        """
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def method(self) -> HTTPRequestMethod:  # dead: disable
        """Indicate the desired action to be performed for a given resource."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def body(self) -> str:  # dead: disable
        """Content sent by the client."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def headers(self) -> Dict[str, str]:
        """Additional information with an HTTP request or response."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def cookies(self) -> Dict[str, str]:
        """Small piece of data that a server gets from the user's web browser."""
        raise NotImplementedError()
