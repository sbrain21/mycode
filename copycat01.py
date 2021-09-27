#!/usr/bin/env python3

# Code to move files around

#importing code to assist with the job
import shutil
import os

# defining the function

def main():

# move into the working directory
os.chdir("/home/student/mycode/")

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")

#call the function to make the backup
main()

