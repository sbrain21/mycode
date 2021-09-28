#!/usr/bin/env python3

# importing tools
import shutil
import os

# specify where program to start
os.chdir('/home/student/mycode/')

# moving files
shutil.move('raynor.obj', 'ceph_storage/')

# rename new file and execute the move
xname = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

