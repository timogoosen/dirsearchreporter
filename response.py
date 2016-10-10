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





    def read_and_print(filename):

        with open(filename,'r') as fd:
            a = ''
            for line in fd.readlines():
                a = a + line

            return a

    def do_other_stuff(line):
        for f in line.split():
            print(f)


    def loop_over_first(line):
    # Split lines so we can count how many entries we have
        split_lines = line.split()
    # Get length of split entries so like "404 30kb http://url.com" should have lengg
    th of 3
        fileRows = []
        line_length = len(split_lines)
        for f in range(1,line_length,3):
            print(split_lines[f])
