package name.qidong.leetcode;

/**
 * Given a 32-bit signed integer, reverse digits of an integer.
 * <p>
 * <strong>Example 1:</strong>
 * <pre><code>
 * Input: 123
 * Output:  321
 * </code></pre>
 * <strong>Example 2:</strong>
 * <p>
 * <pre><code>
 * Input: -123
 * Output: -321
 * </code></pre>
 * <p>
 * <strong>Example 3:</strong>
 * <p>
 * <pre><code>
 * Input: 120
 * Output: 21
 * </code></pre>
 * <p>
 * <strong>Note:</strong> Assume we are dealing with an environment which could only hold integers
 * within the 32-bit signed integer range. For the purpose of this problem, assume that your
 * function returns 0 when the reversed integer overflows.
 *
 * @see <a href="https://leetcode.com/problems/reverse-integer/">Reverse Integer - LeetCode</a>
 */
public class ReverseInteger {
    public int reverse(int x) {
        if (x == Integer.MIN_VALUE) {
            return 0;
        }

        int sign = x < 0 ? -1 : 1;
        x *= sign;
        int unsigned = 0;
        while (x != 0) {
            int bits = calc_bits(unsigned);
            if (bits + 3 >= 32) {
                return 0;
            }

            unsigned *= 10;

            if (unsigned < 0) {
                return 0;
            }

            unsigned += x % 10;
            x /= 10;
        }
        return unsigned * sign;
    }

    private int calc_bits(int num) {
        int bits = 0;
        while (num != 0) {
            ++bits;
            num >>= 1;
        }
        return bits;
    }
}
