#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['s', 'expect']
rows = [
    ('the sky is blue', 'blue is sky the'),
    ('  hello world!  ', 'world! hello'),
    ('a good   example', 'example good a'),
    ('', ''),
    (' ', ''),
    ('word', 'word'),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows)
