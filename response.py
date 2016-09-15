#!/usr/bin/env python3


import sqlite3
import os


class ReportReader(object):

    # This is almost the inverse of this: https://github.com/maurosoria/dirsearch/blob/master/lib/reports/BaseReport.py
    # we loop over directories in dirsearch/reports and read text file reports

    # Can get some ideas of how to read files in directory from here: https://github.com/jekyc/wig/blob/master/wig/classes/cache.py
    #
    # Usage:
    #
    # from response import ReportReader
    #
    # reportreader = ReportReader()
    #
    # path_to_reports = input("Where is the path to the reports directory for dirsearch usually it is located at ~/dirsearch/reports. ")
    # list_of_dirs = []
    # list_of_dirs = reportreader.get_directory_list(path_to_reports)
    #
    #
    #
    def get_directory_list(path):
        # path = "/home/timo/diresearch/reports"
        #
        dirlist = []

        for f in os.listdir(path):

        # Maybe append dir name to path so you will have full path ?
            dirlist.append(f)



        return dirlist




    def get_file_list(directory):

        # Get list of files in directory so we can read the contents of each.






class CheckResponses(object):


    def find_junk_responses():
        # Look for 10 or more
        # response 200's with the same response size
        #

    # Stuff Related to Logging dirsearch to sqlite
    #
    #
    def discard_junk_responses():

    def setup_tables(self, conn):

        cur = conn.cursor()
