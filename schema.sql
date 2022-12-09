CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	ref_type TEXT, -- no args for this
	identifier TEXT,
	author TEXT,
	editor TEXT,
	title TEXT,
	publisher TEXT,
	year INTEGER
);

-- Websites
CREATE TABLE misc (
	id SERIAL PRIMARY KEY,
	ref_type TEXT, -- no args for this, misc
	identifier TEXT,
	title TEXT,
	editor TEXT, -- REALLY AUTHOR
	how_published TEXT, -- no _ in bibtex
	year INTEGER,
	note TEXT
);

CREATE TABLE tags (
	id SERIAL PRIMARY KEY,
	tag_text TEXT
);

CREATE TABLE work_tag_pairs (
	id SERIAL PRIMARY KEY,
	citation_identifier TEXT UNIQUE,
	tag_id INTEGER REFERENCES tags

);
