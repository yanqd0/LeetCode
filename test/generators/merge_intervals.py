#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['intervals', 'expect']
rows = [
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 2], [3, 4], [2, 3]], [[1, 4]]),
    ([[1, 2], [3, 4], [5, 6], [2, 3], [4, 5]], [[1, 6]]),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows)
