import glob
import random
from os.path import split

read_files = glob.glob("C:/Users/sec113/Downloads/birads/ftr_binary/*.txt")

rads="BiradsCategory"
c=0
f=random.sample(read_files,599)
while c<1:
    for i in f:
        f_name = split(i)[-1]
        f_file=open(i).read()
        c_count=str.count(f_file,rads,0)
        c=c+c_count
        if c<=608:
            print f_name,c_count,c,"TrainingSet"
        if c>608 and c<=709:
            print  f_name,c_count,c,"DevelopmentSet"
        if c>709:
            print  f_name,c_count,c,"TestingSet"

print c

