#!/usr/bin/env python3
"""Using CSV library to work with CSV data"""

# import library
import csv

# open the file source csv_users.txt
with open("csv_users.txt", "r") as csvfile:
    # counter to create file names
    counter = 0
    # loop thru file line by line
    for line in csv.reader(csvfile):
        counter = counter + 1
        filename = f"admin.rc{counter}" # creates the file name

        # write data to indivdual files
        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL=" + line[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + line[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + line[2], file=rcfile)
            print("export OS_USERNAME=" + line[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + line[4], file=rcfile)
            print("export OS_PASSWORD=" + line[5], file=rcfile)
print('all files completed')

