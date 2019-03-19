CREATE TABLE users (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
UNIQUE(name)
);

CREATE TABLE cases (
id SERIAL PRIMARY KEY,
question_id INTEGER REFERENCES questions (id),
case_text VARCHAR(100),
trueness BOOLEAN
);

CREATE TABLE questions (
id SERIAL PRIMARY KEY,
question_contest VARCHAR(250)
);

CREATE TABLE test (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
UNIQUE(name)
);

CREATE TABLE test_contest (
test_id INTEGER REFERENCES test (id),
question_id INTEGER REFERENCES questions (id),
UNIQUE(question_id)
);

CREATE TABLE users_answers (
user_id INTEGER REFERENCES users (id),
test_id INTEGER REFERENCES test (id),
question_id INTEGER REFERENCES questions (id),
case_id INTEGER REFERENCES cases (id),
UNIQUE(user_id, test_id, question_id, case_id)
);