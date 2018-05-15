import csv
import re
from os.path import abspath, basename, dirname, join


def read_csv(path, parser=None):
    path = abspath(path)
    name = basename(path)
    name = re.sub('^test_', '', name)
    name = re.sub('py$', 'csv', name)
    cases = join(dirname(path), 'cases')
    csv_path = join(cases, name)

    with open(csv_path) as fobj:
        reader = csv.reader(fobj)
        result = []
        for line in reader:
            if reader.line_num == 1:
                continue
            new_line = [(parser(item) if parser else item) for item in line]
            result.append(new_line)
        return result
