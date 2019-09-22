#!/usr/bin/env python
# -*- coding:utf-8 -*-

FIELDS = ['nums', 'target', 'expect']
ROWS = [
    ('', '', set()),
    (' ', '  ', set()),
    ('apple', '', {'apple'}),
    ('apple apple', 'banana', {'banana'}),
    ('apple apple', 'banana banana', set()),
    ('apple', 'banana', {'apple', 'banana'}),
    ('this apple is sweet', 'this apple is sour', {'sweet', 'sour'}),
    ('  this apple is sweet', 'this apple is sour  ', {'sweet', 'sour'}),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, FIELDS, ROWS)
