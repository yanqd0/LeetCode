#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['input_str', 'expect']
rows = [
    ('42', 42),
    ('   -42', -42),
    ('4193 with words', 4193),
    ('words and 987', 0),
    ('-91283472332', -2 ** 31),
    ('+42', 42),
    ('+91283472332', 2 ** 31 - 1),
    ('', 0),
    ('   ', 0),
    ('-', 0),
]

if __name__ == '__main__':
    from __utils import generate_csv

    generate_csv(__file__, fields, rows, quote_empty=True)
