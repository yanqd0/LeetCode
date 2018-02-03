from leetcode.add_two_numbers import ListNode, Solution

SOLUTION = Solution()


def test_add_two_numbers0():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = SOLUTION.addTwoNumbers(l1, l2)
    assert 7 == result.val
    assert 0 == result.next.val
    assert 8 == result.next.next.val


def test_add_two_numbers1():
    l1 = ListNode(5)
    l2 = ListNode(5)

    result = SOLUTION.addTwoNumbers(l1, l2)
    assert 0 == result.val
    assert 1 == result.next.val


def test_add_two_numbers2():
    l1 = cursor = ListNode(9)
    for index in range(9):
        cursor.next = ListNode(9)
        cursor = cursor.next
    l2 = ListNode(1)

    cursor = SOLUTION.addTwoNumbers(l1, l2)
    for index in range(10):
        assert 0 == cursor.val
        cursor = cursor.next
    assert 1 == cursor.val
