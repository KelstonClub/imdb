import os, sys
import csv
import gzip

with gzip.open("title.basics.tsv.gz") as gf:
    text = (line.decode("utf-8") for line in gf)
    reader = csv.reader(text, delimiter="\t")

    with open("2021-titles.tsv", "w", newline="") as fout:
        writer = csv.writer(fout, delimiter="\t")

    for n, line in enumerate(reader):
        if line[1] == "movie" and line[5] == "2021":
            print(line)
