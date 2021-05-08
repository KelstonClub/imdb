import gzip
import pprint
import csv

def data_from_file(filename):
    file = gzip.open(filename)
    rows = (line.decode("utf-8") for line in file)
    csv_reader = csv.reader(rows, delimiter="\t")
    for n, row in enumerate(csv_reader):
        yield row
        if n > 100: break
    #~ return csv_reader

def dictionary_of_data(filename):
    return dict((row[0], row) for row in data_from_file(filename))

names = dictionary_of_data("name.basics.tsv.gz")
titles = dictionary_of_data("title.basics.tsv.gz")
principals = dictionary_of_data("title.principals.tsv.gz")

