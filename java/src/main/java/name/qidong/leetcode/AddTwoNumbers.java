package name.qidong.leetcode;

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
 * @see <a href="https://leetcode.com/problems/add-two-numbers/">Add Two Numbers - LeetCode</a>
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = l1;
        int carry = 0;
        for (ListNode cursor = result; cursor != null; cursor = cursor.next) {
            cursor.val = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
            carry = cursor.val / 10;
            cursor.val %= 10;

            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
            cursor.next = l1 != null ? l1 : l2;
            cursor.next = (cursor.next == null && carry != 0) ? new ListNode(0) : cursor.next;
        }
        return result;
    }

    /**
     * Definition for singly-linked list.
     * <pre>
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     * </pre>
     */
    public static class ListNode {
        public int val;
        public ListNode next;

        public ListNode(int x) {
            val = x;
        }
    }
}
