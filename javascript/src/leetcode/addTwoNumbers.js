/**
 * You are given two non-empty linked lists representing two non-negative integers. The digits are
 * stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
 * return it as a linked list.
 * <p>
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * <p>
 * Example
 * <pre>
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 * </pre>
 *
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 *
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let result = l1;
  let carry = 0;
  for (let cursor = result; cursor != null; cursor = cursor.next) {
    cursor.val = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
    carry = cursor.val < 10 ? 0 : 1;
    cursor.val %= 10;

    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;
    cursor.next = l1 || l2;
    cursor.next = (cursor.next === null && carry !== 0) ? new ListNode(0) : cursor.next;
  }
  return result;
};

/*
Runtime: 104 ms, faster than 96.55% of JavaScript online submissions for Add Two Numbers.
Memory Usage: 39 MB, less than 20.57% of JavaScript online submissions for Add Two Numbers.
*/

class ListNode {
  constructor (val) {
    this.val = val;
    this.next = null;
  }
}

export default addTwoNumbers;
