package name.qidong.leetcode;

/**
 * Given a string, find the length of the <strong>longest substring</strong> without repeating
 * characters.
 * <p>
 * <strong>Examples:</strong>
 * <p>
 * Given <code>"abcabcbb"</code>, the answer is <code>"abc"</code>, which the length is 3.
 * <p>
 * Given <code>"bbbbb"</code>, the answer is <code>"b"</code>, with the length of 1.
 * <p>
 * Given <code>"pwwkew"</code>, the answer is <code>"wke"</code>, with the length of 3. Note that
 * the answer must be a <strong>substring</strong>, <code>"pwke"</code> is a subsequence and not a
 * substring.
 *
 * @see <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">
 * Longest Substring Without Repeating Characters - LeetCode</a>
 */
@SuppressWarnings("SpellCheckingInspection")
public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int last = -1;
        int[] char2index = new int[128];
        for (int i = 0; i < s.length(); ++i) {
            int previous = char2index[s.charAt(i)];
            if (previous > 0) {
                max = Math.max(max, i - last - 1);
                for (int j = last + 1; j < previous; ++j) {
                    char2index[s.charAt(j)] = -1;
                }
                last = previous - 1;
            }
            char2index[s.charAt(i)] = i + 1;
        }
        return Math.max(max, s.length() - last - 1);
    }
}

/*
Runtime: 2 ms, faster than 99.87% of Java online submissions
for Longest Substring Without Repeating Characters.
Memory Usage: 36.6 MB, less than 99.83% of Java online submissions
for Longest Substring Without Repeating Characters.
*/
