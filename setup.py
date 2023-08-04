#!/usr/bin/env python


import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="test-service",
    version="1.0",
    description="A Python/SQL test framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src", exclude=["tests"]),
    install_requires=[],
    extras_require={},
    zip_safe=True,
)
