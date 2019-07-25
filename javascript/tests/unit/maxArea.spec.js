import { readCases } from './utils';
import maxArea from '../../src/leetcode/maxArea';

const CASES = readCases('container_with_most_water.csv');

describe('maxArea.js', () => {
  test.each(CASES)('height=%s, expect=%s', (height, expected) => {
    expect(expected).toEqual(maxArea(height));
  });
});
