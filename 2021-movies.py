#!.venv\scripts\python.exe
import gzip, csv

file = gzip.open("title.basics.tsv.gz")
rows = (line.decode("utf-8") for line in file)
csv_reader = csv.reader(rows, delimiter="\t")

def get_movies():
    for row in csv_reader:
        if row[1] == "movie":
            if row[5] == "2021":
                yield row

with open("2021-titles.csv", "w", newline = "", encoding = "utf-8") as write_file:
    csv_writer = csv.writer(write_file)
    movies = get_movies()
    csv_writer.writerows(movies)
