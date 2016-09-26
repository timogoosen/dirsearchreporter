#!/usr/bin/env python3

from response import ReportReader

reportreader = ReportReader()

path_to_reports = input("Where is the path to the reports directory for dirsearch usually it is located at ~/dirsearch/reports. ")
list_of_dirs = []
list_of_dirs = reportreader.get_directory_list(path_to_reports)

# Loop over dirs then for each directory get list of files in directory
print(list_of_dirs)

list_of_files = []
