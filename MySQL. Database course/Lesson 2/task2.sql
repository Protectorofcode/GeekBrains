DROP TABLE IF EXISTS users;
CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Name'
) COMMENT = 'Simple table';

INSERT INTO users VALUES
  (DEFAULT, 'Dima'),
  (DEFAULT, 'Nastya'),
  (DEFAULT, 'Vika');