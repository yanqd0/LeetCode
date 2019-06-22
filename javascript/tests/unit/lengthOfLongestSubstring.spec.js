import { readCases } from './utils';
import lengthOfLongestSubstring from '../../src/leetcode/lengthOfLongestSubstring';

const CASES = readCases('longest_substring_without_repeating_characters.csv', [String, Number]);

describe('lengthOfLongestSubstring.js', () => {
  test.each(CASES)('s=%s, expect=%s', (s, expected) => {
    expect(expected).toEqual(lengthOfLongestSubstring(s));
  });
});
