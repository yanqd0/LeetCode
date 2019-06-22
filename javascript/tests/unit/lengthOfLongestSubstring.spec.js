import { readCases } from './utils';
import lengthOfLongestSubstring from '../../src/leetcode/lengthOfLongestSubstring';

// eslint-disable-next-line no-eval
const CASES = readCases('longest_substring_without_repeating_characters.csv', [String, Number]);

describe('addTwoNumbers.js', () => {
  test.each(CASES)('s=%s, expect=%s', (s, expected) => {
    expect(expected).toEqual(lengthOfLongestSubstring(s));
  });
});
