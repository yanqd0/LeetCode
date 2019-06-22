#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['x', 'expect']
rows = [
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
    (1, True),
    (-1, False),
    (123321, True),
    (123324, False),
    (123341, False),
    (123421, False),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows)
