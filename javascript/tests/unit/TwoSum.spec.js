import fs from 'fs';
import path from 'path';
import parse from 'csv-parse/lib/sync';
import { twoSum } from '../../src/leetcode/TwoSum';

const CSV_NAME = 'two_sum.csv';
const CSV_FILE = path.join(__dirname, 'cases', CSV_NAME);
const CSV_CONTENT = fs.readFileSync(CSV_FILE, { encoding: 'utf-8' });
const CASES = parse(CSV_CONTENT, { columns: false, skip_empty_lines: true }).slice(1);
const TESTS = [];
for (let params of CASES) {
  let parsed = [];
  for (let param of params) {
    // eslint-disable-next-line no-eval
    parsed.push(eval(param));
  }
  TESTS.push(parsed);
}

describe('TwoSum.js', () => {
  test.each(TESTS)('nums=%s, target=%s, expect=%s', (nums, target, expected) => {
    expect(expected).toEqual(twoSum(nums, target));
  });
});
