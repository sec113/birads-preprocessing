__author__ = 'SergioMC'

import csv
import glob
from itertools import groupby
from os.path import join, split


# Replacing the BI-RADS expert annotations by a binary category, store this files in a new folder
in_folder = glob.glob('C:/Users/sec113/Downloads/birads/ftr/*.txt')
# folder ftr3 is filled with the binary birads classification
out_folder = 'C:/Users/sec113/Downloads/birads/ftr_binary'
move_folder = 'C:/Users/sec113/Downloads/birads/move'

exp_birads = ['LeftBirads','RightBirads','MultiLateralBirads','NonSpecificBirads','OverAllBirads']
bn_birads = 'BiradsCategory'

for i in in_folder:
    file_name = split(i)[-1]
    outie = join(out_folder, file_name)
    outie2 = join(move_folder,file_name)
    final_file=open(i, 'rb').read()
    for element in exp_birads:
        final_file=final_file.replace(element, bn_birads)
    with open(outie, 'wb') as outfile:
        print>>outfile, final_file
    with open(outie2,'wb') as outfile:
         print>>outfile, final_file

# move all the files to their respective folders
import os
os.system("C:/Users/sec113/Downloads/birads/move.bat")

# checking there is a BiradsCategory in all the documents.
import glob
read_files = glob.glob("C:/Users/sec113/Downloads/birads/ftr_binary/*.txt")

for i in read_files:
    if 'BiradsCategory' in open(i).read():
        print i, "true"
    else:
        print i, "false"


# Create the training set that it will be used by MALLET
import glob
read_files = glob.glob("C:/Users/sec113/Downloads/birads/training_set/*.txt")

with open("C:/Users/sec113/Downloads/birads/training_set.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

#all reports in one document
import glob
read_files = glob.glob("C:/Users/sec113/Downloads/birads/ftr_binary/*.txt")

with open("C:/Users/sec113/Downloads/birads/result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

#Run Mallet from Python
import subprocess
import os

os.chdir('C:\\mallet')
#output_file = open('C:/Users/sec113/Downloads/birads/crf_outputs.txt','wb')
mallet_crf = subprocess.call('java -cp "C:\mallet\class;C:\mallet\lib\mallet-deps.jar" cc.mallet.fst.SimpleTagger --train true --model-file "C:\Users\sec113\Downloads/birads/birads_test.model" "C:\Users\sec113\Downloads/birads/training_set.txt">output_f.txt',shell=True)