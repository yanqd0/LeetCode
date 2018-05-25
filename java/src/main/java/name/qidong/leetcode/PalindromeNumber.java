package name.qidong.leetcode;

/**
 * Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same
 * backward as forward.
 * <p>
 * Example 1:
 * <pre>
 * Input: 121 Output: true
 * </pre>
 * Example 2:
 * <pre>
 * Input: -121 Output: false Explanation: From left to right, it reads -121. From right to left, it
 * becomes 121-. Therefore it is not a palindrome.
 * </pre>
 * Example 3:
 * <pre>
 * Input: 10 Output: false Explanation: Reads 01 from right to left. Therefore it is not a
 * palindrome.
 * </pre>
 * Follow up:
 * <p>
 * Could you solve it without converting the integer to a string?
 *
 * @see <a href="https://leetcode.com/problems/palindrome-number/">Palindrome Number - LeetCode</a>
 */
public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        if (x < 10) return true;

        int high = (int) Math.log10(x);
        int low = 0;
        while (low < high) {
            if (numberOf(x, low) == numberOf(x, high)) {
                low++;
                high--;
            } else {
                return false;
            }
        }
        return true;
    }

    private int numberOf(int x, int digit) {
        int num = (int) Math.pow(10, digit);
        return x / num % 10;
    }
}
