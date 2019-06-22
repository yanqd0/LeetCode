#!/usr/bin/env python
# -*- coding:utf-8 -*-

MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31

fields = ['input_str', 'expect']
rows = [
    ('42', 42),
    ('   -42', -42),
    ('4193 with words', 4193),
    ('words and 987', 0),
    ('-91283472332', MIN_INT),
    ('+91283472332', MAX_INT),
    ('+42', 42),
    ('', 0),
    ('   ', 0),
    ('-', 0),
    ('-13+1', -13),
    ('  0000000000012345678', 12345678),
    ('-000000000000001', -1),
    ('+000000000000001', 1),
    (" -1010023630o4", -1010023630),
    (" +1010023630o4", 1010023630),
    ('20000000000000000000', MAX_INT),
    ('+20000000000000000000', MAX_INT),
    ('-20000000000000000000', MIN_INT),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows, quote_empty=True)
