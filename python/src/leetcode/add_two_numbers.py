"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = cursor = l1
        carry = 0
        while cursor is not None:
            cursor.val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = cursor.val // 10
            cursor.val %= 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cursor.next = l1 if l1 else l2
            if not cursor.next and carry:
                cursor.next = ListNode(0)
            cursor = cursor.next
        return result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
