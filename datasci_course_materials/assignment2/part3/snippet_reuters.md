sqlite> select * from sqlite_master;

table|Frequency|Frequency|2|CREATE TABLE Frequency (
docid VARCHAR(255),
term VARCHAR(255),
count int,
PRIMARY KEY(docid, term))
index|sqlite_autoindex_Frequency_1|Frequency|10010|

sqlite> select * from Frequency LIMIT 5;

docid         |term|count

10000_txt_earn| net|1
10000_txt_earn| rogers|4
10000_txt_earn| earnings|2
10000_txt_earn| switch|1
10000_txt_earn| conn|1
