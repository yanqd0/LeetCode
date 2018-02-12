from pytest import mark

from leetcode.reverse_integer import MAX_INT, MIN_INT, Solution

# noinspection SpellCheckingInspection
PARAMS = [
    (1, 1),
    (120, 21),
    (123, 321),
    (-123, -321),
    (1534236469, 0),
    (9646324351, 0),
    (MAX_INT, 0),
    (MIN_INT, 0),
]


@mark.parametrize('x, expect', PARAMS)
def test_longest_palindrome(x, expect):
    solution = Solution()
    assert expect == solution.reverse(x)
