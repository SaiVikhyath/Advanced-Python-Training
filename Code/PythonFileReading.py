"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

import glob
import os

"""
Illustration of opening and reading files in Python
"""


# Reading a file from the top
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head('./movies.xml', 10)
print()


# Reading a file from the bottom
def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize - 1
            data = []
            while True:
                iter += 1
                f.seek(fsize - bufsize * iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break


file_read_from_tail('./movies.xml', 10)


# Reading a file into an object
def file_read(fname):
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        content_list = f.readlines()
        print(len(content_list))
        print(content_list)


file_read('./StateOfTheUnion.txt')

char_list = []
files_list = glob.glob("./movies.xml")
for file_elem in files_list:
    with open(file_elem, "r") as f:
        char_list.append(f.read())
print(char_list)
