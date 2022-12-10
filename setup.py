from setuptools import setup
import os

VERSION = "0.3.1"


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
    url="https://datasette.io/plugins/datasette-render-binary",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-render-binary/issues",
        "CI": "https://github.com/simonw/datasette-render-binary/actions",
        "Changelog": "https://github.com/simonw/datasette-render-binary/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_render_binary"],
    entry_points={"datasette": ["export = datasette_render_binary"]},
    install_requires=["datasette", "filetype"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
