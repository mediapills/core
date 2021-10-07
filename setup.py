import setuptools

# for pip >= 10
try:
    from pip._internal.req import parse_requirements
    from pip._internal.network.session import PipSession
# for pip <= 9.0.3
except ImportError:
    from pip.req import parse_requirements  # type: ignore
    from pip.network.session import PipSession  # type: ignore

version = "0.0.3.rc1"

requirements = parse_requirements("requirements.txt", session=PipSession())

install_requires = [
    str(i.requirement if hasattr(i, "requirement") else i.req)  # type: ignore
    for i in requirements
]

setuptools.setup(version=version, install_requires=install_requires)
