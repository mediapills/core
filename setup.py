import setuptools
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

version = "0.0.3"

requirements = parse_requirements("requirements.txt", session=PipSession())

install_requires = [str(requirement.req) for requirement in requirements]  # type: ignore

setuptools.setup(version=version, install_requires=install_requires)
