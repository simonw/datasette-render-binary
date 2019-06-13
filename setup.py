from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-render-binary",
    description="Datasette plugin for rendering binary data",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-render-binary",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_render_binary"],
    entry_points={"datasette": ["render_binary = datasette_render_binary"]},
    install_requires=["datasette", "filetype"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette-render-binary[test]"],
)
