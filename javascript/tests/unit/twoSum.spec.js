import { readCases } from './utils';
import twoSum from '../../src/leetcode/twoSum';

const CASES = readCases('two_sum.csv');

describe('twoSum.js', () => {
  test.each(CASES)('nums=%s, target=%s, expect=%s', (nums, target, expected) => {
    expect(expected).toEqual(twoSum(nums, target));
  });

  test('twoSum.js invalid input', () => {
    expect(() => twoSum([1, 2], 4)).toThrow(Error);
  });
});
