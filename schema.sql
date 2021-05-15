/*
 *
 * title.basics.tsv.gz - Contains the following information for titles:

    tconst (string) - alphanumeric unique identifier of the title
    titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
    primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
    originalTitle (string) - original title, in the original language
    isAdult (boolean) - 0: non-adult title; 1: adult title
    startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
    endYear (YYYY) – TV Series end year. ‘\N’ for all other title types
    runtimeMinutes – primary runtime of the title, in minutes
    genres (string array) – includes up to three genres associated with the title
 */

DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS basics;

CREATE TABLE genres (
	tconst VARCHAR NOT NULL,
	genre1 VARCHAR,
	genre2 VARCHAR,
	genre3 VARCHAR
);

CREATE TABLE basics (
	tconst VARCHAR NOT NULL,
	titleType VARCHAR,
	primaryTitle VARCHAR,
	originalTitle VARCHAR,
	isAdult BOOL,
	startYear VARCHAR,
	endYear VARCHAR,
	runtimeMinutes INT,
	genres VARCHAR,
	FOREIGN KEY(genres) REFERENCES genres(tconst)
);
