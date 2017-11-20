CREATE TABLE indledger (
  indledger_id SERIAL,
  user_id varchar(20),
  full_name VARCHAR(50) NOT NULL,
  address VARCHAR(50),
  phoneno VARCHAR(50),
  lock BOOLEAN,
  panno VARCHAR(20),
  create_date timestamp NULL,
  modify_date timestamp NULL,
  remarks1 VARCHAR(200) NULL,
  remarks2 VARCHAR(200) NULL,

  PRIMARY KEY(indledger_id)
);
