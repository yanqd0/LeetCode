#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['height', 'expect']
rows = [
    ([1, 1], 1),
    ([1, 2], 1),
    ([1, 2, 3, 4, 5], 6),
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 8, 6, 2, 5, 4, 8, 3, 6], 42),
    ([1, 8, 6, 2, 5, 4, 8, 8, 6], 48),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows)
