CREATE TABLE grpledger (
  grpledger_id SERIAL,
  user_id varchar(20),
  name  VARCHAR(50) UNIQUE NOT NULL,
  type CHAR(1),
  liquidity CHAR(1),
  cashbank CHAR(1),
  is_system CHAR(1),
  have_subledger CHAR(1),
  create_date timestamp NULL,
  modify_date timestamp NULL,
  remarks1 VARCHAR(200) NULL,
  remarks2 VARCHAR(200) NULL,
 
  PRIMARY KEY(grpledger_id)
);
