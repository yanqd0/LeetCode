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
 * @see <a href="https://leetcode.com/problems/longest-palindromic-substring/">Longest Palindromic
 * Substring - LeetCode</a>
 */
@SuppressWarnings("SpellCheckingInspection")
public class LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        final int len = s.length();
        if (len < 2) {
            return s;
        }

        int start = 0, end = 0;
        for (int fix = 0; fix < 2; ++fix) {
            int center = (len - 1) / 2;
            for (int step = 0; step < len; ++step) {
                center += (step + fix) % 2 == 1 ? step : -step;
                int padding = Math.min(center, len - 1 - center - fix);
                if (2 * padding + fix < end - start) {
                    break;
                }

                boolean palindrom = true;
                for (int half = 0; half <= padding; ++half) {
                    if (s.charAt(center - half) != s.charAt(center + fix + half)) {
                        --half;
                        if (2 * half + fix > end - start 
                                || 2 * half + fix == end - start && center - 1 - half < start) {
                            start = center - half;
                            end = center + fix + half;
                        }
                        palindrom = false;
                        break;
                    }
                }

                if (palindrom) {
                    start = center - padding;
                    end = center + fix + padding;
                }
            }
        }
        return s.substring(start, end + 1);
    }
}

/*
Runtime: 6 ms, faster than 88.02% of Java online submissions for Longest Palindromic Substring.
Memory Usage: 36 MB, less than 99.98% of Java online submissions for Longest Palindromic Substring.
*/