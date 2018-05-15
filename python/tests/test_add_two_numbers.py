from pytest import mark

from leetcode.add_two_numbers import ListNode, Solution
from . import read_csv

SOLUTION = Solution()


def _parser(item):
    sep = '->'
    if sep in item:
        root = last = None
        for value in item.split(sep):
            node = ListNode(int(value))
            if last:
                last.next = node
                last = last.next
            else:
                root = last = node
        return root
    else:
        return ListNode(int(item))


@mark.parametrize('l1, l2, expect', read_csv(__file__, parser=_parser))
def test_add_two_numbers(l1, l2, expect):
    result = Solution().addTwoNumbers(l1, l2)
    while expect or result:
        assert expect.val == result.val
        expect = expect.next
        result = result.next
