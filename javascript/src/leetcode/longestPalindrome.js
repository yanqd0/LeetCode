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
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let start = 0;
  let end = 0;
  for (let fix of [0, 1]) {
    let center = Math.floor((s.length - 1) / 2);
    for (let step = 0; step < s.length; ++step) {
      center += (step + fix) % 2 === 1 ? step : -step;
      let padding = Math.min(center, s.length - 1 - center - fix);
      if (2 * padding + fix < end - start) {
        break;
      }

      let palindrom = true;
      for (let half = 0; half <= padding; ++half) {
        if (s.charAt(center - half) !== s.charAt(center + fix + half)) {
          --half;
          if (2 * half + fix > end - start ||
             (2 * half + fix === end - start && center - 1 - half < start)) {
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
};

/*
Runtime: 64 ms, faster than 98.67% of JavaScript online submissions
for Longest Palindromic Substring.
Memory Usage: 35.6 MB, less than 81.32% of JavaScript online submissions
for Longest Palindromic Substring.
*/

export default longestPalindrome;
