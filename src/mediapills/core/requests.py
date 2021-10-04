from abc import ABCMeta
from abc import abstractmethod


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



class BaseRequest(metaclass=ABCMeta):
    @property
    @abstractmethod
    def body(self):

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def json(self):

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def args(self):

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def headers(self):

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def form(self):

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def method(self):

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def url_root(self):

        raise NotImplementedError  # pragma: no cover

    @property
    @abstractmethod
    def url(self):

        raise NotImplementedError  # pragma: no cover
