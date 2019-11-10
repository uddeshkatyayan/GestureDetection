import sys

text = ''
filename = sys.argv[1]
with open(filename) as f:
    for line in f.readlines():
    	if ".jpg" in line:
    	   if "right" in line:
    	   	label = '1'
    	   elif "left" in line:
    	   	label = '2'
    	   elif "center" in line:
    	   	label = '3'
    	   text += '"'+line[:-1]+'", '+label+'\n'
with open(filename[:-4]+'_out.csv','w+') as f:
	f.write(text)
