#!/usr/bin/env python
# -*- coding:utf-8 -*-

FIELDS = ['nums', 'k', 'expect']
ROWS = [
    ([1], 1, 1),
    ([1, 1], 1, 1),
    ([1, 1], 2, 1),
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, FIELDS, ROWS)
