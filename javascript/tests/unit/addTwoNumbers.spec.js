import { readCases } from './utils';
import addTwoNumbers, { ListNode } from '../../src/leetcode/addTwoNumbers';

function parser (str) {
  // eslint-disable-next-line no-eval
  const list = eval(str);
  const head = new ListNode(0);
  let cursor = head;
  for (let value of list) {
    cursor.next = new ListNode(value);
    cursor = cursor.next;
  }
  return head.next;
}
const CASES = readCases('add_two_numbers.csv', [parser, parser, parser]);

describe('addTwoNumbers.js', () => {
  test.each(CASES)('l1=%s, l2=%s, expect=%s', (l1, l2, expected) => {
    expect(expected).toEqual(addTwoNumbers(l1, l2));
  });
});
