#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['nums', 'target', 'expect']
rows = [
    ([1, 1], 2, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 2, 3], 6, [0, 2]),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows)
