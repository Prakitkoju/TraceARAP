CREATE TABLE tblitems (
  item_id SERIAL,
  user_id varchar(20),
  name VARCHAR(50) NOT NULL,
  type VARCHAR(50),
  sales_rate decimal(18,2),
  purchase_rate decimal(18,2),
  lock BOOLEAN,
  create_date timestamp NULL,
  modify_date timestamp NULL, 
  remarks1 VARCHAR(200) NULL,
  remarks2 VARCHAR(200) NULL,

  PRIMARY KEY(item_id)
);
