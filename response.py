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
            dir_list.append(f)



        return dir_list




    def get_file_list(self):

        file_list = []

        current_dir = os.getcwd()


        for f in os.listdir(current_dir):


            file_list.append(f)

        return file_list





    def open_file(self,filename):
        # Do Stuff
        #
        print ("We will open the file here")
