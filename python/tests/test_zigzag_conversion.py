from pytest import mark

from leetcode.zigzag_conversion import Solution

# noinspection SpellCheckingInspection
PARAMS = [
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


@mark.parametrize('s, rows, expect', PARAMS)
def test_longest_palindrome(s, rows, expect):
    solution = Solution()
    assert expect == solution.convert(s, rows)
