from pandas import DataFrame
import glob
from os.path import join, split

# take out all the features and have one token per line, these documents will be used for the CRF model
# perhaps you should just create this folder using the raw documents to have a token per line this way you could have it quicker in a different folder

in_files   = glob.glob('C:/Users/sec113/Downloads/birads/dev_set/*.txt')
output_dir  = 'C:/Users/sec113/Downloads/birads/ftr5'

for i in in_files:
    file_name = split(i)[-1]
    output_path = join(output_dir, file_name)
    with open(output_path, 'wb') as outf:
        data1 = DataFrame.from_csv(i,sep=' ',parse_dates=False)
        data2=DataFrame(data=data1.index,index=None)
        data2.to_csv(output_path, sep=' ', index=False)
