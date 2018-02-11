PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE authors ( id integer primary key autoincrement, name text not nul
l, birth date);                                                              
INSERT INTO authors VALUES(1,'John','1980-12-25');
INSERT INTO authors VALUES(2,'Mike','1976-9-4');
CREATE TABLE books (id integer primary key autoincrement, title text not null,
 author_id integer not null, published_in date, foreign key (author_id) refere
nces authors(id));                                                           
INSERT INTO books VALUES(1,'My life with Anna',1,'2004-3-6');
INSERT INTO books VALUES(2,'Bye, bye, Anna',1,'2004-6-6');
INSERT INTO books VALUES(3,'Wonderful Anna',2,'2005-1-2');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('authors',2);
INSERT INTO sqlite_sequence VALUES('books',3);
COMMIT;
