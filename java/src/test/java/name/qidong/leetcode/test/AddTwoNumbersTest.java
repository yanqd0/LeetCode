package name.qidong.leetcode.test;

import name.qidong.leetcode.AddTwoNumbers;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static name.qidong.leetcode.AddTwoNumbers.ListNode;
import static org.junit.jupiter.api.Assertions.assertEquals;

class AddTwoNumbersTest {
    private AddTwoNumbers solution;

    @BeforeEach
    void setUp() {
        solution = new AddTwoNumbers();
    }

    @Test
    void addTwoNumbers0() {
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        ListNode result = solution.addTwoNumbers(l1, l2);
        assertEquals(7, result.val);
        assertEquals(0, result.next.val);
        assertEquals(8, result.next.next.val);
    }

    @Test
    void addTwoNumbers1() {
        ListNode l1 = new ListNode(5);
        ListNode l2 = new ListNode(5);
        ListNode result = solution.addTwoNumbers(l1, l2);
        assertEquals(0, result.val);
        assertEquals(1, result.next.val);
    }

    @Test
    void addTwoNumbers2() {
        ListNode l1 = new ListNode(9);
        ListNode cursor = l1;
        for (int i = 0; i < 9; ++i) {
            cursor.next = new ListNode(9);
            cursor = cursor.next;
        }
        ListNode l2 = new ListNode(1);

        cursor = solution.addTwoNumbers(l1, l2);

        for (int i = 0; i < 10; ++i) {
            assertEquals(0, cursor.val);
            cursor = cursor.next;
        }
        assertEquals(1, cursor.val);
    }
}