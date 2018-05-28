#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['s', 'p', 'expect']
rows = [
    ('aa', 'a', False),
    ('aa', 'a*', True),
    ('ab', '.*', True),
    ('aab', 'c*a*b', True),
    ('mississippi', 'mis*is*p*.', False),
    ('mississippi', 'mis*is*.p*.', True),
    ('mississippi', '.*', True),
    ('', '', True),
    ('aaaabbbb', 'a*ab*', True),
    ('aaaabbbb', 'a*.ab*', True),
    ('aaaabbbb', 'a*aab*', True),
    ('aaaabbbb', '.a*ab*', True),
    ('aaaabbbb', 'aaaaa*b*bbbb', True),
    ('aaaabbbb', '.aab*', False),
    ('aaaabbbb', '........', True),
    ('aaaabbbb', '.......', False),
]

if __name__ == '__main__':
    from __utils import generate_csv

    generate_csv(__file__, fields, rows)
