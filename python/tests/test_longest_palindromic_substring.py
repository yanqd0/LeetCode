from pytest import mark

from leetcode.longest_palindromic_substring import Solution

# noinspection SpellCheckingInspection
PARAMS = [
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
]


@mark.parametrize('input_str, expect', PARAMS)
def test_longest_palindrome(input_str, expect):
    solution = Solution()
    assert expect == solution.longestPalindrome(input_str)
