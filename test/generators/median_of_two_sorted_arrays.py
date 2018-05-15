#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['num1', 'num2', 'expect']
rows = [
    ([], [1], 1.0),
    ([2], [], 2.0),
    ([2], [1, 3, 4], 2.5),
    ([1, 2, 4], [3], 2.5),
    ([3], [1, 2], 2.0),
    ([2], [1, 3, 4, 5], 3.0),
    ([4], [1, 2, 3, 5], 3.0),
    ([1, 4], [2, 3, 5, 6, 7], 4.0),
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([1, 3], [2, 4], 2.5),
    ([2, 3], [1, 4], 2.5),
    ([1], [3], 2.0),
    ([1], [1, 2, 3, 4], 2.0),
    ([9], [1, 2, 3, 4], 3.0),
    ([1, 2, 3, 4, 5, 6], [1, 2], 2.5),
    ([1, 2, 3, 4, 5, 6], [3, 4], 3.5),
    ([1, 2, 3, 4, 5, 6], [5, 6], 4.5),
    ([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8, 9], 5.0),
    ([1, 2, 3, 4, 8, 9], [3, 4, 5, 6, 7, 8, 9], 5.0),
]

if __name__ == '__main__':
    from __utils import generate_csv

    generate_csv(__file__, fields, rows)
