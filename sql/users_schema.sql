CREATE TABLE users (
  user_id SERIAL,
  user_name VARCHAR(50) NOT NULL,
  org_name VARCHAR(50) NOT NULL,
  org_address VARCHAR(50),
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL,
  create_date timestamp NULL,
  modify_date timestamp NULL,
  lock BOOLEAN,
  remarks1 VARCHAR(200),
  remarks2 VARCHAR(200),

  PRIMARY KEY(user_id)
);
