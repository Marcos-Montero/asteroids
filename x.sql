ALTER TABLE users
  ADD COLUMN country_code TEXT NOT NULL DEFAULT 'KH';

ALTER TABLE users
  ADD COLUMN country_name TEXT NOT NULL DEFAULT 'Kingdom of Hearts';

UPDATE users
SET country_code = (SELECT country_code FROM countries WHERE countries.id = users.country_id),
    country_name = (SELECT name FROM countries WHERE countries.id = users.country_id);

ALTER TABLE users
  DROP COLUMN country_id;

CREATE INDEX country_code_idx ON users(country_code);

DROP TABLE countries;

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

SELECT * FROM users;

