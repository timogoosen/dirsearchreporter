#!/usr/bin/env python3

from response import ReportReader
import os

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
        reportreader.loop_over_first(filehandle)
    #print (file_list)
    # This works fine unless there is a file between all the directories in the reports/ directory.
    # Need to have a check to see if something is a file or directory.





#list_of_files = []
