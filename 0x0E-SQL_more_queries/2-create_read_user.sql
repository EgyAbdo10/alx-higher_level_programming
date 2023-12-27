-- creating a db and a user
-- creating a db
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grantong a read_only permission to a user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';