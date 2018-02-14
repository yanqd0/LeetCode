package name.qidong.leetcode;

/**
 * Given a string s, find the longest palindromic substring in s. You may assume that the maximum
 * length of s is 1000.
 * <p>
 * Example:
 * <pre><code>
 * Input: "babad"
 *
 * Output: "bab"
 * </code></pre>
 * Note: "aba" is also a valid answer.
 * <p>
 * Example:
 * <pre><code>
 * Input: "cbbd"
 *
 * Output: "bb"
 * </code></pre>
 *
 * @see <a href="https://leetcode.com/problems/longest-palindromic-substring/description/">Longest
 * Palindromic Substring - LeetCode</a>
 */
@SuppressWarnings("SpellCheckingInspection")
public class LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        final int len = s.length();
        if (len <= 1) {
            return s;
        }
        int start = 0, end = 0;

        int index = len / 2;
        for (int step = 0; step < len; ++step) {
            index += step % 2 == 1 ? step : -step;
            int padding = Math.min(index, len - 1 - index);
            if (end - start > 2 * padding) {
                break;
            }

            boolean palindrom = true;
            for (int half = 0; half <= padding; ++half) {
                if (s.charAt(index + half) != s.charAt(index - half)) {
                    --half;
                    if (2 * half > end - start
                            || 2 * half == end - start && index - half < start) {
                        start = index - half;
                        end = index + half;
                    }
                    palindrom = false;
                    break;
                }
            }
            if (palindrom) {
                start = index - padding;
                end = index + padding;
            }
        }

        index = len / 2;
        for (int step = 0; step <= len; ++step) {
            index += step % 2 == 1 ? step : -step;
            int padding = Math.min(index - 1, len - 1 - index);
            if (end - start > 2 * padding + 1) {
                break;
            }

            boolean palindrom = true;
            for (int half = 0; half <= padding; ++half) {
                if (s.charAt(index - 1 - half) != s.charAt(index + half)) {
                    --half;
                    if (2 * half + 1 > end - start
                            || 2 * half + 1 == end - start && index - 1 - half < start) {
                        start = index - 1 - half;
                        end = index + half;
                    }
                    palindrom = false;
                    break;
                }
            }
            if (palindrom) {
                start = index - 1 - padding;
                end = index + padding;
            }
        }

        return s.substring(start, end + 1);
    }
}
