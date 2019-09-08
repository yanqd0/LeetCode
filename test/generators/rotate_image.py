#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['matrix', 'expect']
rows = [
    ([[1]], [[1]]),
    ([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ], [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]),
    ([
        [ 5,  1,  9, 11],  # noqa: E201
        [ 2,  4,  8, 10],  # noqa: E201
        [13,  3,  6,  7],
        [15, 14, 12, 16],
    ], [
        [15, 13,  2,  5],
        [14,  3,  4,  1],
        [12,  6,  8,  9],
        [16,  7, 10, 11],
    ]),
]  # yapf: disable

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows)
