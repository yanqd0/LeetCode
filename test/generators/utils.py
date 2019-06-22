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
        writer = csv.DictWriter(fobj, fieldnames=fields, lineterminator='\n')
        writer.writeheader()

    with open(csv_path, 'a') as fobj:
        quoting = csv.QUOTE_NONNUMERIC if quote_empty else csv.QUOTE_MINIMAL
        writer = csv.writer(fobj, quoting=quoting, lineterminator='\n')
        writer.writerows(rows)
