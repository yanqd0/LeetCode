#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['test_str', 'expect']
rows = [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('c', 1),
    ('', 0),
    ('au', 2),
    ('aab', 2),
    ('abba', 2),
    ('ggububgvfk', 6),
    ('cdd', 2),
]

if __name__ == '__main__':
    from __utils import generate_csv

    generate_csv(__file__, fields, rows)
