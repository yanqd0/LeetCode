from pytest import mark

from leetcode.add_two_numbers import ListNode, Solution

from . import read_csv


def _parser(item):
    nodes = eval(item)
    head = ListNode(0)
    cursor = head
    for value in nodes:
        cursor.next = ListNode(value)
        cursor = cursor.next
    return head.next


@mark.parametrize('l1, l2, expect', read_csv(__file__, parser=_parser))
def test_add_two_numbers(l1, l2, expect):
    result = Solution().addTwoNumbers(l1, l2)
    while expect or result:
        assert expect.val == result.val
        expect = expect.next
        result = result.next
