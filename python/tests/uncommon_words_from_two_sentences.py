from pytest import mark

from leetcode.uncommon_words_from_two_sentences import Solution

from . import read_csv


@mark.parametrize('a, b, expect', read_csv(__file__))
def test_two_sum(a, b, expect):
    result = Solution().uncommonFromSentences(a, b)
    assert set(result) == eval(expect)
