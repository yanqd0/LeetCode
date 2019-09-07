#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" Setup script for leetcode.py """
import runpy

from setuptools import find_packages, setup

_INFO = runpy.run_path('src/leetcode/_meta.py')
_SETUP_REQUIRES = [
    'pytest-runner',
    'setuptools-scm',
]
_TESTS_REQUIRE = [
    'pytest',
    'pytest-cov',
    'pytest-isort',
    'pytest-yapf3',
]

setup(
    # Metadata
    name='leetcode.py',
    description='Python solutions of LeetCode',
    url=_INFO['__url__'],
    author=_INFO['__author__'],
    author_email=_INFO['__email__'],
    license=_INFO['__license__'],
    use_scm_version={
        'root': '..',
        'relative_to': __file__,
    },
    # Package modules and data
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # Requires
    python_requires='>=3.6',
    install_requires=[],
    setup_requires=_SETUP_REQUIRES,
    tests_require=_TESTS_REQUIRE,
    extras_require={
        'dev': _SETUP_REQUIRES + _TESTS_REQUIRE,
    },
    # PyPI Metadata
    keywords=['leetcode'],
    platforms=['any'],
    classifiers=[
        # see: https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
