import csv
import sys

with open(sys.argv[1], 'rt') as f:
    with open(sys.argv[2], 'wt') as o:
        reader = csv.reader(f)
        writer = csv.writer(o)
        for row in reader:
            changed_row = [s.replace('|', ',') for s in row]
            # print(row)
            # # changed_row = str(row).replace('|', ',')
            # print(changed_row)
            writer.writerow(changed_row)

            