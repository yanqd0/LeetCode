#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['l1', 'l2', 'expect']
rows = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([5], [5], [0, 1]),
    ([9] * 9, [1], [0] * 9 + [1]),
]

if __name__ == '__main__':
    from __utils import generate_csv

    generate_csv(__file__, fields, rows)
