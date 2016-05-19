__author__ = 'SergioMC'
import glob
import csv
from itertools import groupby
from os.path import join, split

# We don't have duplicate rows anymore
# Remove the duplicate rows from the original XMI output and stores those files in a new document
IN_FILE   = glob.glob('C:/Users/sec113/Downloads/birads/ftr/*.txt')
# folder ftr and ftr2 contains the multiclass birads classification
OUT_DIR  = 'C:/Users/sec113/Downloads/birads/ftr2'

for i in IN_FILE:
    f_name = split(i)[-1]
    out_path = join(OUT_DIR, f_name)
    with open(out_path, 'wb') as outf:
        datalist= open(i, 'rb').readlines()
        incsv  = csv.reader(datalist, delimiter=" ")
        outcsv = csv.writer(outf, delimiter=" ")
        # Read data and de-duplicate
        # ! assumes data is already in sorted order !
        for word,rows in groupby(incsv, key=lambda row: row[0:2]):
            outcsv.writerow(next(rows))