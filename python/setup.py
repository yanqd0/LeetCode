#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" Setup script for csft """
import runpy

from setuptools import find_packages, setup


INFO = runpy.run_path('src/leetcode/_meta.py')

setup(
    name='leetcode',
    description='Python solutions of LeetCode',

    url=INFO['__url__'],
    author=INFO['__author__'],
    author_email=INFO['__email__'],
    license=INFO['__license__'],
    use_scm_version={
        "root": "..",
        "relative_to": __file__,
    },

    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': (
            'csft = csft.__main__:main',
        ),
    },

    python_requires='>=3.6',
    install_requires=[],
    setup_requires=[
        'pytest-runner >= 3.0',
        'setuptools_scm >= 2.0.0',
    ],
    tests_require=[
        'pytest >= 3.4.0',
        'pytest-cov >= 2.5.1',
        'pytest-mock >= 1.10.0',
    ],

    keywords=['leetcode'],
    platforms=['any'],
    classifiers=[
        # see: https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],
)
