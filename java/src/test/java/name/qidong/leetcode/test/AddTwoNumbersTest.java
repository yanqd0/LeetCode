package name.qidong.leetcode.test;

import name.qidong.leetcode.AddTwoNumbers;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.extension.ParameterContext;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.converter.ArgumentConversionException;
import org.junit.jupiter.params.converter.ArgumentConverter;
import org.junit.jupiter.params.converter.ConvertWith;
import org.junit.jupiter.params.provider.CsvFileSource;

import static name.qidong.leetcode.AddTwoNumbers.ListNode;
import static org.junit.jupiter.api.Assertions.assertEquals;

class AddTwoNumbersTest {
    private AddTwoNumbers solution;

    @BeforeEach
    void setUp() {
        solution = new AddTwoNumbers();
    }

    @ParameterizedTest
    @CsvFileSource(resources = "/add_two_numbers.csv", numLinesToSkip = 1)
    void addTwoNumbers(
            @ConvertWith(String2ListNode.class) ListNode l1,
            @ConvertWith(String2ListNode.class) ListNode l2,
            @ConvertWith(String2ListNode.class) ListNode expect
    ) {
        solution = new AddTwoNumbers();
        ListNode result = solution.addTwoNumbers(l1, l2);
        while (expect != null || result != null) {
            assertEquals(expect.val, result.val);
            expect = expect.next;
            result = result.next;
        }
    }
}

class String2ListNode implements ArgumentConverter {
    @Override
    public Object convert(Object source, ParameterContext context)
            throws ArgumentConversionException {
        try {
            String str = (String) source;
            final String sep = "->";
            if (str.contains(sep)) {
                ListNode root = null, last = null;
                for (String value : str.split(sep)) {
                    ListNode node = new ListNode(Integer.parseInt(value.trim()));
                    if (last == null) {
                        root = last = node;
                    } else {
                        last = last.next = node;
                    }
                }
                return root;
            } else {
                return new ListNode(Integer.parseInt(str.trim()));
            }
        } catch (ClassCastException e) {
            throw new ArgumentConversionException("The source is not a String", e);
        } catch (NumberFormatException e) {
            throw new ArgumentConversionException("Some content in source is not int", e);
        }
    }
}