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
from pathlib import Path

import setuptools

_ROOT = Path(__file__).resolve().parent
version = "0.0.3rc1"


def _read_install_requires() -> list[str]:
    """Return dependency specifiers from requirements.txt"""
    path = _ROOT / "requirements.txt"
    text = path.read_text(encoding="utf-8")
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if line:
            lines.append(line)
    return lines


def _read_long_description() -> str:
    return (_ROOT / "README.md").read_text(encoding="utf-8")


setuptools.setup(
    name="mediapills.core",
    version=version,
    description="Small domain-oriented micro-kernel primitives.",
    long_description=_read_long_description(),
    long_description_content_type="text/markdown",
    license_expression="MIT",
    license_files=["LICENSE.md"],
    url="https://github.com/mediapills/core",
    project_urls={
        "Homepage": "https://github.com/mediapills/core",
        "Issues": "https://github.com/mediapills/core/issues",
    },
    author="Andrew Yatskovets",
    author_email="andriy.yatskovets@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="patterns,kernel,use-case,entity,controller,domain-driven",
    python_requires=">=3.5",
    install_requires=_read_install_requires(),
    packages=setuptools.find_namespace_packages(where="src"),
    package_dir={"": "src"},
    platforms=["any"],
    include_package_data=True,
)
