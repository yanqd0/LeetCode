#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['x', 'expect']
rows = [
    (1, True),
    (121, True),
    (-121, False),
    (10, False),
]

if __name__ == '__main__':
    from __utils import generate_csv

    generate_csv(__file__, fields, rows)
