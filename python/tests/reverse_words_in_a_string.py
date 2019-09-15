from pytest import mark, raises

from leetcode.reverse_words_in_a_string import Solution

from . import read_csv


@mark.parametrize('s, expect', read_csv(__file__, parser=str))
def test_two_sum(s, expect):
    assert expect == Solution().reverseWords(s)
