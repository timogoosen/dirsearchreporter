#!/usr/bin/env python3

from response import ReportReader
import os
from sqlitelogger import SQLiteLogger
import sqlite3


# Some things to be able to log to sqlite
logger = SQLiteLogger()

database = "challenge.sqlite"

conn = logger.connection(database)
logger.setup_tables(conn)


# To be able to use methods to parse and process data

reportreader = ReportReader()

path_to_reports = input("Where is the path to the reports directory for dirsearch usually it is located at ~/dirsearch/reports. ")
list_of_dirs = []
list_of_dirs = reportreader.get_directory_list(path_to_reports)

#current_dir = os.getcwd()

# Loop over dirs then for each directory get list of files in directory
#print(list_of_dirs)


for f in list_of_dirs:
    dir_path = path_to_reports + "/" + f
    # Gives full absoluate dir path for example
    # /home/timo/blah/+
    #print (dir_path)
    # List files here.
    file_list = []
    file_list = reportreader.get_file_list(dir_path)

    for i in file_list:
        file_path_for_file = dir_path + "/" + i
        #print(file_path_for_file)
        filehandle = reportreader.read_and_print(file_path_for_file)
        filerows_first = []
        filerows_second = []
        filerows_third = []

        filerows_first = reportreader.loop_over_first(filehandle)
        filerows_second = reportreader.loop_over_second(filehandle)
        filerows_third = reportreader.loop_over_third(filehandle)


        #Get Length of array so we can loop over it
        file_length = len(filerows_first)
    #    file_length_second = len(filerows_second)
    #    file_length_third = len(filerows_third)

        #print(file_length_first,file_length_second,file_length_third)



        for a in range(1,file_length):

            # Strip the B from for example 292B of content size so it
            # will be 292 instead. Thus we can better work with the values as int in sqlite


            # content_size = convert_to_byte(content_Size_string)

            content_size = reportreader.convert_to_byte(filerows_first[a])
            #a = a[:-1]



            request_url = filerows_second[a]
            status_code = filerows_third[a-1]

            #print(content_size,request_url,status_code)
            logger.load_statuscode_table(status_code, conn)
            logger.load_file_table(request_url, 1, content_size, status_code, conn)

# Close database only after all files rusults have been imported
logger.close_conection(conn)
