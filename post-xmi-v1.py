__author__='SergioMC'
import csv
import glob
from itertools import groupby
from os.path import join, split

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

# Replacing the BI-RADS expert annotations by a binary category, store this files in a new folder
in_folder = glob.glob('C:/Users/sec113/Downloads/birads/ftr2/*.txt')
# folder ftr3 is filled with the binary birads classification
out_folder = 'C:/Users/sec113/Downloads/birads/ftr_binary'

exp_birads = ['LeftBirads','RightBirads','MultiLateralBirads','NonSpecificBirads','OverAllBirads']
bn_birads = 'BiradsCategory'

for i in in_folder:
    file_name = split(i)[-1]
    outie = join(out_folder, file_name)
    final_file=open(i, 'rb').read()
    for element in exp_birads:
        final_file=final_file.replace(element, bn_birads)
    with open(outie, 'wb') as outfile:
        print>>outfile, final_file

# checking there is a BiradsCategory in all the documents.
import glob
read_files = glob.glob("C:/Users/sec113/Downloads/birads/ftr_binary/*.txt")

for i in read_files:
    if 'BiradsCategory' in open(i).read():
        print i, "true"
    else:
        print i, "false"


import glob
read_files = glob.glob("C:/Users/sec113/Downloads/birads/ftr_binary/*.txt")

with open("C:/Users/sec113/Downloads/birads/result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

#basic stats

# Select the Impression section only

#y = [ a for a in in_folder if a[2] == 'Impression' ]
#print y