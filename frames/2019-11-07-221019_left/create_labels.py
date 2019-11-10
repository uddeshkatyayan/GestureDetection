import sys

text = ''
filename = sys.argv[1]
label = sys.argv[2]
with open(filename) as f:
    for line in f.readlines():
    	if ".jpg" in line:
    	   text += '"'+line[:-1]+'", '+str(label)+'\n'
with open(filename[:-4]+'_out.csv','w+') as f:
	f.write(text)
