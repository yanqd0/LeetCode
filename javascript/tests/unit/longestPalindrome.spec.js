import { readCases } from './utils';
import longestPalindrome from '../../src/leetcode/longestPalindrome';

const CASES = readCases('longest_palindromic_substring.csv', [String, String]);

describe('longestPalindrome.js', () => {
  test.each(CASES)('s=%s, expect=%s', (s, expected) => {
    expect(expected).toEqual(longestPalindrome(s));
  });
});
