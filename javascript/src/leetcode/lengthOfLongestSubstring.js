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
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let max = 0;
  let last = 0;
  const char2index = new Array(128);
  for (let i = 0; i < s.length; ++i) {
    let next = char2index[s.charCodeAt(i)];
    if (next) {
      max = Math.max(max, i - last);
      for (let j = last; j < next; ++j) {
        char2index[s.charCodeAt(j)] = undefined;
      }
      last = next;
    }
    char2index[s.charCodeAt(i)] = i + 1;
  }
  return Math.max(max, s.length - last);
};

/*
Runtime: 64 ms, faster than 99.95% of JavaScript online submissions
for Longest Substring Without Repeating Characters.
Memory Usage: 37.5 MB, less than 94.85% of JavaScript online submissions
for Longest Substring Without Repeating Characters.
*/

export default lengthOfLongestSubstring;
