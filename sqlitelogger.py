#!/usr/bin/env python


import sqlite3


class SQLiteLogger(object):

    # Stuff Related to Logging dirsearch to sqlite

    def setup_tables(self, conn):

        cur = conn.cursor()
    # The count we can work out by doing a select of File.name,id where name =
    # name.

        cur.executescript('''

        DROP TABLE IF EXISTS StatusCode;
        DROP TABLE IF EXISTS File;


        PRAGMA foreign_keys = ON;

        CREATE TABLE StatusCode (
            code INTEGER primary key,
            codecount INTEGER
        );

        CREATE TABLE File (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            file           TEXT,
            requestcount     INTEGER default 1,
            contentlength      INTEGER,
          statuscode INTEGER,
            FOREIGN KEY(statuscode) REFERENCES StatusCode(code)
        );




        ''')

    def connection(self, db):
        conn = sqlite3.connect(db)
        return conn

    def close_conection(self, conn):
        conn.close()

    def load_statuscode_table(self, statuscode, conn):
        cur = conn.cursor()

    # Everytime I connect to database run this query
    # PRAGMA foreign_keys = ON;
    # Turns foreign key support on
        cur.execute('''PRAGMA foreign_keys = ON''')

    # Check if statuscode was added before
    # This returns 1 if it exists
    # select exists(select code from StatusCode where code=404)
        # Maybe insert or ignore
        cur.execute(
            '''select exists(select code from StatusCode where code=?)''', ( int(statuscode), ) )
        exists = cur.fetchone()[0]

        if exists:
            print ("StatusCode already exists")
            # Use update to update count increment current count by one.
            # Can increment like this:
            # UPDATE StatusCode set codecount = codecount+1 WHERE code = 200;
            cur.execute(
                '''UPDATE StatusCode set codecount = codecount+1 WHERE code = ?''', ( int(statuscode), ) )

        else:
            print ("StatusCode does not exist lets insert it into db")
            cur.execute('''INSERT OR IGNORE INTO StatusCode (code,codecount)
        VALUES ( ?,1 )''', ( int(statuscode), ) )

        # Catch error here

        # Commit Changes
        conn.commit()

        # INSERT INTO StatusCode(code,codecount) VALUES (500,1);

        # If it exists then we update the count.

    # Load File  inserting into file table.

    def load_file_table(self, file, requestcount, contentlength, statuscode, conn):
        cur = conn.cursor()

        cur.execute('''PRAGMA foreign_keys = ON''')

        # Does value exist in StatusCode table yet?

        # Insert into statement

        # INSERT Into File(id,file,requestcount,contentlength,statuscode)
        # VALUES(4,"/server-status.php","1","3432","404");

        cur.execute('''INSERT OR IGNORE INTO FILE (file,requestcount,contentlength,statuscode)
                VALUES (?, ?, ?, ? )''', (  file, int(requestcount), int(contentlength), int(statuscode)) )

        # Remember to commit

        conn.commit()

    # Parse CSV

    # Use this baby
