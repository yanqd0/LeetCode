#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['nums', 'val', 'expect', 'new_nums']
rows = [
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
    ([1, 1, 1, 1], 1, 0, []),
    ([1, 1, 1, 1], 2, 4, [1, 1, 1, 1]),
    ([1, 2, 3, 4], 2, 3, [1, 3, 4]),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows)
