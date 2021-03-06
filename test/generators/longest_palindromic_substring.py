#!/usr/bin/env python
# -*- coding:utf-8 -*-

fields = ['input_str', 'expect']
rows = [
    ('', ''),
    ('a', 'a'),
    ('abb', 'bb'),
    ('ccd', 'cc'),
    ('cbbd', 'bb'),
    ('aaaab', 'aaaa'),
    ('abbbb', 'bbbb'),
    ('babad', 'bab'),
    ('aaaaab', 'aaaaa'),
    ('abbbbb', 'bbbbb'),
    ('ababababccd', 'abababa'),
    ('abcdefgfedcba', 'abcdefgfedcba'),
    ('abcdefg', 'a'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaa'),
]

if __name__ == '__main__':
    from utils import generate_csv

    generate_csv(__file__, fields, rows, quote_empty=True)
