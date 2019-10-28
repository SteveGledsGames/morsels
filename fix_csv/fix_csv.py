from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    rows = list(csv.reader(old_file, delimiter='|'))

with open(args.new_filename, mode='wt', newline='') as new_file:
    csv.writer(new_file).writerows(rows)