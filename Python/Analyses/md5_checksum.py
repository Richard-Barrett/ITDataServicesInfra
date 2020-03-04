#!/bin/python 
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: md5 Checksum to Compare Files
# Date: 03/04/2020
# ===========================================================

import hashlib, sys
files = [sys.argv[1], sys.argv[2]] #these are the arguments we take
def md5(fname):
    md5hash = hashlib.md5()
    with open(fname) as handle: #opening the file one line at a time for memory considerations
        for line in handle:
            md5hash.update(line.encode('utf-8'))
    return(md5hash.hexdigest())
print('Comparing Files:',files[0],'and',files[1])
if md5(files[0]) == md5(files[1]):
    print('Matched')
else:
    print('Not Matched')
