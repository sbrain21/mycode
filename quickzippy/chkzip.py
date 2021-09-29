#!/usr/bin/python3

"""script to check if a file is a zip or not"""

import zipfile

#create variable for the filename to be checked

file = input('What file do you want to check?')

#main code
def main():
    if zipfile.is_zipfile(file):
        print('Yes this is a zip file')
    else:
        print('No, this is not a zip file.')

main()

