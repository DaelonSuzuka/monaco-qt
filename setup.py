#! /usr/bin/env python
# -*- coding: utf-8 -*-


from pathlib import Path
from setuptools import setup, find_packages


here = Path(__file__).parent


DESCRIPTION = "The Monaco editor as a Qt Widget"
LONG_DESCRIPTION = (here / "README.md").read_text()
CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Widget Sets",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]


setup(
    name="monaco-qt",
    version="0.1.5",
    packages=find_packages(),
    install_requires=[
        'QtPy',
    ],
    package_data={'monaco': ['*.js', '*.html', 'monaco-editor/**']},
    include_package_data=True,
    # setup_requires=[],
    # tests_require=[],
    platforms=["any"],
    author="David Kincaid",
    author_email="dlkincaid0@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=CLASSIFIERS,
    keywords=[
        "qtstrap",
        "qt",
        "pyqt",
        "monaco",
        "text editor",
    ],
    url="https://github.com/DaelonSuzuka/monaco-qt"
)