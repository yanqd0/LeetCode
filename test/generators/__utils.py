import csv
import re
from os import makedirs
from os.path import abspath, basename, dirname, isdir, join


def generate_csv(path, fields, rows, quote_empty=False):
    path = abspath(path)
    name = basename(path)
    name = re.sub('py$', 'csv', name)
    cases = join(dirname(dirname(path)), 'cases')
    if not isdir(cases):
        makedirs(cases)
    csv_path = join(cases, name)

    with open(csv_path, 'w') as fobj:
        writer = csv.DictWriter(fobj, fieldnames=fields)
        writer.writeheader()

    with open(csv_path, 'a') as fobj:
        if quote_empty:
            writer = csv.writer(fobj, quoting=csv.QUOTE_NONNUMERIC)
        else:
            writer = csv.writer(fobj)
        writer.writerows(rows)
