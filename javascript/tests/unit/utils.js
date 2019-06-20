import fs from 'fs';
import path from 'path';
import parse from 'csv-parse/lib/sync';

export function readRawCases (name) {
  const csvFile = path.join(__dirname, 'cases', name);
  const content = fs.readFileSync(csvFile, { encoding: 'utf-8' });
  return parse(content, { columns: false, skip_empty_lines: true }).slice(1);
}

export function parseParameters (cases, parsers = null) {
  const parsedCases = [];
  if (!parsers) {
    // Use `eval` as the default parameter parser.
    // eslint-disable-next-line no-eval
    parsers = cases[0].map(x => eval);
  }
  for (let row of cases) {
    let parsed = [];
    for (let i in row) {
      let parser = parsers[i];
      parsed.push(parser(row[i]));
    }
    parsedCases.push(parsed);
  }
  return parsedCases;
}

export function readParsedCases (name, parsers = null) {
  const cases = readRawCases(name);
  return parseParameters(cases, parsers);
}

export const readCases = readParsedCases;
