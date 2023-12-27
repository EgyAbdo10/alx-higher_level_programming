-- create a user and give it all privileges
-- creating
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- granting privileges
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';