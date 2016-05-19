__author__ = 'SergioMC'

import glob
import os
from os.path import join, split, exists

input_files = glob.glob('C:/Users/sec113/Downloads/raw2/*.txt')
xml_files = glob.glob('C:/Users/sec113/Downloads/expert/*.birads.sec113.completed.xml')
output_dir = 'C:/Users/sec113/Downloads/bayes_ftr'
if not exists(output_dir):
    os.makedirs(output_dir)

for i in input_files:
    file_name = split(i)[-1]
    output_path = join(output_dir, file_name)
    with open(output_path,'wb') as outfile:
        datalist= open(i, 'rb').readlines()
        for j, line in enumerate(datalist):
            outfile.write('{0:<5}{1}'.format(j+1, line))

