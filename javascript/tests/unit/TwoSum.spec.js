import { readCases, parseParameters } from './utils';
import twoSum from '../../src/leetcode/twoSum';

const RAW_CASES = readCases('two_sum.csv');
const CASES = parseParameters(RAW_CASES);

describe('TwoSum.js', () => {
  test.each(CASES)('nums=%s, target=%s, expect=%s', (nums, target, expected) => {
    expect(expected).toEqual(twoSum(nums, target));
  });

  test('Invalid input', () => {
    expect(() => twoSum([1, 2], 4)).toThrow(Error);
  });
});
