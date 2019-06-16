from pytest import mark

from leetcode.string_to_integer_atoi import Solution

from . import read_csv


@mark.parametrize('input_str, expect', read_csv(__file__))
def test_add_two_numbers(input_str, expect):
    expect = int(expect)
    result = Solution().myAtoi(input_str)
    assert expect == result
