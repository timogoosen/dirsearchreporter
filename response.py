#!/usr/bin/env python3


import sqlite3
import os



class ReportReader(object):

    # This is almost the inverse of this: https://github.com/maurosoria/dirsearch/blob/master/lib/reports/BaseReport.py
    # we loop over directories in dirsearch/reports and read text file reports

    # Can get some ideas of how to read files in directory from here: https://github.com/jekyc/wig/blob/master/wig/classes/cache.py
    #
    # Usage:



#    from response import ReportReader

#    reportreader = ReportReader()

#    path_to_reports = input("Where is the path to the reports directory for dirsearch usually it is located at ~/dirsearch/reports. ")
#    list_of_dirs = []
#    list_of_dirs = reportreader.get_directory_list(path_to_reports)

#    list_of_files = []
#







    def get_directory_list(self,path):
        # path = "/home/timo/diresearch/reports"
        #
        dir_list = []

        for f in os.listdir(path):

        # Maybe append dir name to path so you will have full path ?
            dir_path = path  + '/' +f
            is_dir = os.path.isdir(dir_path)

            if is_dir:


                dir_list.append(f)



        return dir_list




    def get_file_list(self,path):

        file_list = []


        for f in os.listdir(path):

            file_path = path + '/' +f

            is_file = os.path.isfile(file_path)

            if is_file:


                file_list.append(f)



        return file_list





    def read_and_print(self,filename):

        with open(filename,'r') as fd:
            a = ''
            for line in fd.readlines():
                a = a + line

            return a

    



    def loop_over_first(self,line):
    # Split lines so we can count how many entries we have
        split_lines = line.split()
    # Get length of split entries so like "404 30kb http://url.com" should have length of 3
        fileRows = []
        line_length = len(split_lines)
        for f in range(1,line_length,3):
            #print(split_lines[f])
            fileRows.append(split_lines[f])

        return fileRows


# Loop over third entry in the dirsearch log file
# which is the full url which includes the file that was found e.g https://site.com/install.php

    def loop_over_second(self,line):
    # Split lines so we can count how many entries we have
        split_lines = line.split()
        fileRows = []
        line_length = len(split_lines)
        for f in range(2,line_length,3):
            #print(split_lines[f])
            fileRows.append(split_lines[f])

        return fileRows





    def loop_over_third(self,line):
    # Split lines so we can count how many entries we have
        split_lines = line.split()
        fileRows = []
        line_length = len(split_lines)
        for f in range(3,line_length,3):
            #print(split_lines[f])
            fileRows.append(split_lines[f])

        return fileRows



# Validate and convert
#
# convert to byte value in int
# so from 10KB to 10000
#
# or from 200B to 200B
#
# content_size = convert_to_byte(content_Size_string)
#


    def convert_to_byte(self,content_size_string):

        mb_suffix = "MB"
        kb_suffix = "KB"
        b_suffix = "B"

        if (content_size_string.endswith(mb_suffix)):
                # Convert to int and strip MB at end of string
                # a = a[:-1]
                content_size = int(content_size_string[:-2])
                # Convert to byte by multiplying by 1000000
                return content_size*1000000


        elif (content_size_string.endswith(kb_suffix)):

            content_size = int(content_size_string[:-2])

            return content_size*1000


        elif (content_size_string.endswith(b_suffix)):
            return int(content_size_string[:-1])
