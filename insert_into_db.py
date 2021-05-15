import gzip
import csv
import sqlite3


def data_from_file(filename):
    file = gzip.open(filename)
    rows = (line.decode("utf-8") for line in file)
    csv_reader = csv.reader(rows, delimiter="\t")
    for n, row in enumerate(csv_reader):
        if n == 0: continue
        yield row
        if n >= 1000: break


def dictionary_of_data(filename):
    return dict((row[0], row) for row in data_from_file(filename))


if __name__ == '__main__':
    db = sqlite3.connect('movies.db')
    cur = db.cursor()
    with open('schema.sql', 'r') as f:
        sql = f.read()

    cur.executescript(sql)

    titles = dictionary_of_data("data/title.basics.tsv.gz")
    for title in titles.values():
        title[-1] += ',,,'
        generes = title[-1].split(',')[:3]
        cur.execute(
            "INSERT INTO genres(tconst, genre1, genre2, genre3) VALUES (?, ?, ?, ?)",
            [title[0], *generes])

        title[-1] = title[0]
        if title[6] != '\\N':
            title[6] = int(title[6])
        else:
            title[6] = 0

        cur.execute(
            "INSERT INTO basics(tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            title)

    db.commit()
