#!/usr/bin/env python
# -*- coding:utf-8 -*-

MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31

fields = ['x', 'expect']
rows = [
    (1, 1),
    (120, 21),
    (123, 321),
    (-123, -321),
    (1534236469, 0),
    (MAX_INT, 0),
    (MIN_INT, 0),
]

if __name__ == '__main__':
    from __utils import generate_csv

    generate_csv(__file__, fields, rows)
