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
        filerows_first = []
        filerows_second = []
        filerows_third = []

        filerows_first = reportreader.loop_over_first(filehandle)
        filerows_second = reportreader.loop_over_second(filehandle)
        filerows_third = reportreader.loop_over_third(filehandle)


        #Get Length of array so we can loop over it
        file_length = len(filerows_first)
        #print(file_length)
        for a in range(1,file_length):
            content_size = filerows_first[a]
            request_url = filerows_second[a]
            status_code = filerows_third[a]

            print(content_size,request_url,statuscode)
