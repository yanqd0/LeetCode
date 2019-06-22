#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['s', 'rows', 'expect']
rows = [
    ('', 0, ''),
    ('', 1, ''),
    ('ABC', 0, 'ABC'),
    ('ABC', 1, 'ABC'),
    ('abc', 5, 'abc'),
    ('PAYPALISHIRING', 0, 'PAYPALISHIRING'),
    ('PAYPALISHIRING', 1, 'PAYPALISHIRING'),
    ('PAYPALISHIRING', 2, 'PYAIHRNAPLSIIG'),
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('abcdefghijklmn', 4, 'agmbfhlnceikdj'),
    ('abcdefghijklmn', 5, 'aibhjcgkdflnem'),
    ('abcdefghijklmno', 5, 'aibhjcgkodflnem'),
    ('abcdefghijklmnop', 5, 'aibhjpcgkodflnem'),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows, quote_empty=True)
