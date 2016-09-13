#!/usr/bin/env python3

from sqlitelogger import SQLiteLogger
import sqlite3


logger = SQLiteLogger()



database = "challenge.sqlite"
# Maybe check if database exists
# If it does prompt user and ask if they want to continue

conn = logger.connection(database)
logger.setup_tables(conn)

statuscode = 200
logger.load_statuscode_table(statuscode, conn)

# Load Same status code again should just update the count
#statuscode = 200

statuscode2 = 500
logger.load_statuscode_table(statuscode2, conn)

# Insert into File table
logger.load_file_table("/server-status.php", 1, 343, 500, conn)

logger.close_conection(conn)
