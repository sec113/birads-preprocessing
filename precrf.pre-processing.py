__author__ = 'SergioMC'

import glob
from os.path import join, split
# add Identification for the MARS output and be recognized as a different section.

add = ':'
words = ['[MARS EXAM_TYPE]']

in_file = glob.glob('C:/Users/sec113/Downloads/birads/raw/*.txt')
out_dir = 'C:/Users/sec113/Downloads/birads/raw2'

for i in in_file:
    f_name = split(i)[-1]
    out_path = join(out_dir, f_name)
    f_file=open(i, 'rb').read()
    for word in words:
        f_file=f_file.replace(word, word + add)
    with open(out_path, 'wb') as outfile:
        print>>outfile, f_file
#
        # x=re.sub(r'\b' + word + r'\b', word+add, ifi)
        # print word
        # print x
        # with open(out_path, 'w') as outfile:
        #     print>>outfile, x
#    with open(out_path, 'w') as outfile:
#        outf = re.sub(words, words + add, ifi)
#        print>>outfile, outf


# in_file=open('C:/Users/sec113/Downloads/raw/add2text.txt','rb').read()
# add='::'
# words='\[MARS EXAM_TYPE\]','Addendum begins'

# outf=re.sub(words,words+add,in_file)
# with open('C:/Users/sec113/Downloads/raw/add2text2.txt','w') as outfile:
#    print>>outfile,outf
