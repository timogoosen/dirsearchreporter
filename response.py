#!/usr/bin/env python3


import sqlite3
import os
# -*- coding: utf-8 -*-

class ReportReader(object):

    def get_directory_list(self,path):
        dir_list = []
        for f in os.listdir(path):
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
        split_lines = line.split()
    # Get length of split entries so like "404 30kb http://url.com" should have length of 3
        fileRows = []
        line_length = len(split_lines)
        for f in range(1,line_length,3):
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
            fileRows.append(split_lines[f])
        return fileRows


# Better name for these simliar methods
    def loop_over_third(self,line):
        split_lines = line.split()
        fileRows = []
        line_length = len(split_lines)
        for f in range(3,line_length,3):
            fileRows.append(split_lines[f])
        return fileRows


    def convert_to_byte(self,content_size_string):

        mb_suffix = "MB"
        kb_suffix = "KB"
        b_suffix = "B"

        if (content_size_string.endswith(mb_suffix)):
                content_size = int(content_size_string[:-2])
                return content_size*1000000

        elif (content_size_string.endswith(kb_suffix)):
            content_size = int(content_size_string[:-2])
            return content_size*1000

        elif (content_size_string.endswith(b_suffix)):
            return int(content_size_string[:-1])
