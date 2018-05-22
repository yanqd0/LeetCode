package name.qidong.leetcode;

/**
 * Implement atoi which converts a string to an integer.
 * <p>
 * The function first discards as many whitespace characters as necessary until the first
 * non-whitespace character is found. Then, starting from this character, takes an optional initial
 * plus or minus sign followed by as many numerical digits as possible, and interprets them as a
 * numerical value.
 * <p>
 * The string can contain additional characters after those that form the integral number, which are
 * ignored and have no effect on the behavior of this function.
 * <p>
 * If the first sequence of non-whitespace characters in str is not a valid integral number, or if
 * no such sequence exists because either str is empty or it contains only whitespace characters, no
 * conversion is performed.
 * <p>
 * If no valid conversion could be performed, a zero value is returned.
 * <p>
 * Note:
 * <p>
 * Only the space character ' ' is considered as whitespace character. Assume we are dealing with an
 * environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31
 * − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or
 * INT_MIN (−2^31) is returned.
 * <p>
 * <pre>
 * Example 1:
 *
 * Input: "42"
 * Output: 42
 * </pre>
 * <pre>
 * Example 2:
 *
 * Input: "   -42"
 * Output: -42
 * Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as
 * many numerical digits as possible, which gets 42.
 * </pre>
 * <pre>
 * Example 3:
 *
 * Input: "4193 with words"
 * Output: 4193
 * Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
 * </pre>
 * <pre>
 * Example 4:
 *
 * Input: "words and 987"
 * Output: 0
 * Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/-
 * sign. Therefore no valid conversion could be performed.
 * </pre>
 * <pre>
 * Example 5:
 *
 * Input: "-91283472332"
 * Output: -2147483648
 * Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Therefore
 * INT_MIN (−2^31) is returned.
 * </pre>
 *
 * @see <a href="https://leetcode.com/problems/string-to-integer-atoi/">
 * String to Integer (atoi) - LeetCode</a>
 */
public class StringToIntegerAtoi {
    public int myAtoi(String str) {
        String trimmed = str.trim();
        char[] chars = trimmed.toCharArray();
        int end = 0;
        boolean significance = false;
        for (int sign = 1, zero = 0; end < chars.length; ++end) {
            if (end == 0) {
                if (chars[0] == '-') {
                    sign = -1;
                    continue;
                } else if (chars[0] == '+') {
                    continue;
                }
            } else if (end - zero > 11) {
                return sign > 0 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            if (Character.isDigit(chars[end])) {
                if (chars[end] != '0') {
                    significance = true;
                } else if (!significance) {
                    zero++;
                }
            } else {
                break;
            }
        }
        String numStr = trimmed.substring(0, end);

        long num;
        try {
            num = Long.parseLong(numStr);
        } catch (NumberFormatException e) {
            return 0;
        }

        if (num < Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        } else if (num > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else {
            return (int) num;
        }
    }
}
