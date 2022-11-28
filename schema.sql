CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	ref_type TEXT,
	identifier TEXT,
	author TEXT,
	editor TEXT,
	title TEXT,
	publisher TEXT,
	year INTEGER
)

