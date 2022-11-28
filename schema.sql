CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	ref_type TEXT, -- no args for this
	identifier TEXT,
	author TEXT,
	editor TEXT,
	title TEXT,
	publisher TEXT,
	year INTEGER
)

