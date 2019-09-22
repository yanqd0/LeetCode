#!/usr/bin/env python
# -*- coding:utf-8 -*-

FIELDS = ['nums', 'target', 'expect']
ROWS = [
    ('', '', set()),
    ('apple', '', {'apple'}),
    ('this apple is sweet', 'this apple is sour', {'sweet', 'sour'}),
    ('apple apple', 'banana', {'banana'}),
    ('apple apple', 'banana banana', set()),
    ('apple', 'banana', {'apple', 'banana'}),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, FIELDS, ROWS)
