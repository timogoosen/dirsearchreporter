#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3


class SQLiteLogger(object):

    # Stuff Related to Logging dirsearch to sqlite

    def setup_tables(self, conn):
        cur = conn.cursor()
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
    # We need some methods to validate data especially the content size

    def load_file_table(self, file, requestcount, contentlength, statuscode, conn):
        cur = conn.cursor()
        cur.execute('''PRAGMA foreign_keys = ON''')
        # Does value exist in StatusCode table yet?
        cur.execute(
            '''select exists(select file from File where file=? and statuscode=?)''', ( file,int(statuscode) ) )
        exists = cur.fetchone()[0]
        if exists:
            print ("file already exists increment requestcount for file")
        # Now Update requestcount just look at above code
            cur.execute(
                '''UPDATE File set requestcount = requestcount+1 WHERE file = ? and statuscode=?''', ( file,int(statuscode) ) )
        else:
            cur.execute('''INSERT OR IGNORE INTO FILE (file,requestcount,contentlength,statuscode)
                    VALUES (?, ?, ?, ? )''', (  file, int(requestcount), int(contentlength), int(statuscode)) )


        conn.commit()
